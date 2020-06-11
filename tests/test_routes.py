from starlette.testclient import TestClient

from starlettelab.main import application


def test_home() -> None:
    client = TestClient(application)
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}


def test_hello_jon() -> None:
    client = TestClient(application)
    response = client.get("/hello/jon")

    assert response.status_code == 200
    assert response.json() == {"message": "You know nothing, Jon Snow"}


def test_hello_anonymous() -> None:
    client = TestClient(application)
    response = client.get("/hello/anonymous")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, anonymous!"}


def test_exception_wrong_secret() -> None:
    client = TestClient(application)
    response = client.get("/exception/foo")

    assert response.status_code == 403
    assert response.json() == {"error": "Wrong secret"}


def test_exception_right_secret() -> None:
    # TODO: Mock bugsnag client
    client = TestClient(application, raise_server_exceptions=False)
    response = client.get("/exception/swordfish")

    assert response.status_code == 500
    assert response.text == "Internal Server Error"
