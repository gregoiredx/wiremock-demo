import requests

def test_my_service():
    factor = 3

    response = requests.get(f"http://my-service/multiply-external-service?factor={factor}")

    assert response.status_code == 200
    assert response.json()["result"] == 9
