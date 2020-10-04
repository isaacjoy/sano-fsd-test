# API for user authenticated endpoints
# Note: none of these endpoints should have a user_id or user_email parameter passed in via the request.
# the user_id and user_email is obtained from the JWT, if valid
import io
import json
import logging
from datetime import datetime as dt

import numpy as np
import pytz
import shortuuid
from flask import Blueprint
from flask import current_app as app
from flask import jsonify, request
from peewee import IntegrityError
from playhouse.shortcuts import model_to_dict

from core.auth.decorators import user_only

tz = pytz.timezone("Europe/London")
user_api = Blueprint("user_api", __name__)
logger = logging.getLogger(__name__)

from core.models import Enrollments, Users

# An example user authenticated endpoint.
@user_api.route("/user", methods=["GET"])
@user_only
def get_user(user_id, user_email):
    return jsonify(user_id)

# Get enrollments
@user_api.route("/enrollments", methods=["GET"])
@user_only
def get_enrollments(user_id, user_email):
    user = Users.get(id=user_id)
    enrollments = [enrollment.studies.id for enrollment in user.enrollments]
    return jsonify(enrollments), 200

# Create an enrollment
@user_api.route("/enroll", methods=["POST"])
@user_only
def enroll(user_id, user_email):
    if request.method== 'POST':
        studyID = request.json['study']
        Enrollments.create(user=user_id, studies=studyID)
        return jsonify('Enrolled'), 200

# Delete an enrollment
@user_api.route("/unenroll", methods=["DELETE"])
@user_only
def unenroll(user_id, user_email):
    if request.method== 'DELETE':
        studyID = request.json['study']
        enrollment = Enrollments.get(user=user_id, studies=studyID)
        enrollment.delete_instance()
        return jsonify('Left study'), 200




