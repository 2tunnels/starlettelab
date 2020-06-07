from starlette.testclient import TestClient

from starlettelab.app import application


def test_home():
    client = TestClient(application)
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}
