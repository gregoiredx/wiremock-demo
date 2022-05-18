import flask
import logging
import os
import requests

app = flask.Flask(__name__)

EXTERNAL_SERVICE_URL = os.environ["EXTERNAL_SERVICE_URL"]


@app.route("/multiply-external-service")
def multiply_external_service():
    factor = int(flask.request.args.get("factor", "1"))
    return {"result": factor * _get_external_service_value()}


def _get_external_service_value():
    try:
        external_service_response = requests.get(f"{EXTERNAL_SERVICE_URL}/get-value")
        return external_service_response.json()["value"]
    except requests.exceptions.ConnectionError:
        logging.exception("Error calling external service, let's fallback to 1.")
        return 1
