import flask
import requests

app = flask.Flask(__name__)

@app.route("/multiply-external-service")
def multiply_external_service():
    factor = int(flask.request.args.get("factor", "1"))
    external_service_value = requests.get("http://external-service/get-value").json()["value"]
    return {"result": factor * external_service_value}
