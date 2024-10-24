import pytest

from app.main import app as application


@pytest.fixture
def client():
    application.config["TESTING"] = True
    with application.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hola!!"
