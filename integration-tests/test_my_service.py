import os
import requests

MY_SERVICE_URL = os.environ["MY_SERVICE_URL"]
EXTERNAL_SERVICE_URL = os.environ["EXTERNAL_SERVICE_URL"]


def test_my_service():
    set_external_service_response({"status": 200, "jsonBody": {"value": 3}})
    my_service_factor = 3

    response = requests.get(
        f"{MY_SERVICE_URL}/multiply-external-service?factor={my_service_factor}"
    )

    assert response.status_code == 200
    assert response.json()["result"] == 9

def test_my_service_handles_external_service_downtimes():
    set_external_service_response({"fault": "CONNECTION_RESET_BY_PEER"})
    my_service_factor = 3

    response = requests.get(
        f"{MY_SERVICE_URL}/multiply-external-service?factor={my_service_factor}"
    )

    assert response.status_code == 200
    assert response.json()["result"] == 3

def set_external_service_response(response):
    response = requests.post(
        f"{EXTERNAL_SERVICE_URL}/__admin/mappings",
        json={
            "request": {"method": "GET", "url": "/get-value"},
            "response": response,
        },
    )
    assert response.status_code == 201
