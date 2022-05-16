import os
import requests

MY_SERVICE_URL = os.environ["MY_SERVICE_URL"]

def test_my_service():
    factor = 3

    response = requests.get(f"{MY_SERVICE_URL}/multiply-external-service?factor={factor}")

    assert response.status_code == 200
    assert response.json()["result"] == 9  # static external-service stubs returns 3
