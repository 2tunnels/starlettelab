from starlette.testclient import TestClient

from starlettelab.main import application


def test_foo() -> None:
    client = TestClient(application)
    response = client.get("/")

    assert response.headers["x-foo"] == "yes"
