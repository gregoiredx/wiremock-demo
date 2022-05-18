import flask
import os
import requests

app = flask.Flask(__name__)

EXTERNAL_SERVICE_URL = os.environ["EXTERNAL_SERVICE_URL"]

@app.route("/multiply-external-service")
def multiply_external_service():
    factor = int(flask.request.args.get("factor", "1"))
    external_service_value = requests.get(f"{EXTERNAL_SERVICE_URL}/get-value").json()["value"]
    return {"result": factor * external_service_value}
