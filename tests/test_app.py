from starlette.testclient import TestClient

from starlettelab.app import application


def test_home():
    client = TestClient(application)
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}


def test_hello_jon():
    client = TestClient(application)
    response = client.get("/hello/jon")

    assert response.status_code == 200
    assert response.json() == {"message": "You know nothing, Jon Snow"}


def test_hello_anonymous():
    client = TestClient(application)
    response = client.get("/hello/anonymous")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, anonymous!"}
