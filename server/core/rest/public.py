# API for public endpoints
# Note: think carefully before putting anything in here...
# ...anyone will have access to data exposed from these endpoints

import json
import logging
import zlib
from time import sleep, time

import peewee
import stripe
from dateutil.parser import parse
from flask import Blueprint
from flask import current_app as app
from flask import jsonify, request

from core.auth.store import auth_store
from core.config import config

logger = logging.getLogger(__name__)
public_api = Blueprint("public_api", __name__)

from core.models import Studies
from playhouse.shortcuts import model_to_dict


# -------
# Write you endpoint to retrieve all available studies here.
# -------

@public_api.route("/studies", methods=["GET"])
def get_studies():
    studies = Studies.select()
    studies = [model_to_dict(study) for study in studies]
    return jsonify(studies), 200
