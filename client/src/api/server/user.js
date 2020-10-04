import axios from "axios";

export function get_enrollments() {
    return new Promise((resolve, reject) => {
        axios
            .get("/enrollments")
            .then((response) => {
                resolve(response);
            })
            .catch((error) => {
                reject(error);
            });
    });
}


export function enroll(id) {
    return new Promise((resolve, reject) => {
        axios
            .post("/enroll", {
                'study' : id
            })
            .then((response) => {
                resolve(response);
            })
            .catch((error) => {
                reject(error);
            });
    });
}

export function unenroll(id) {
    return new Promise((resolve, reject) => {
        axios
            .delete("/unenroll", {
                data: {'study' : id}
            })
            .then((response) => {
                resolve(response);
            })
            .catch((error) => {
                reject(error);
            });
    });
}