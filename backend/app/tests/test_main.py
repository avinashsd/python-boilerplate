from collections.abc import Generator
from typing import Any

import pytest
from flask.testing import FlaskClient

from app.main import add
from app.main import app as application


@pytest.fixture
def client() -> Generator[FlaskClient, Any, Any]:
    application.config["TESTING"] = True
    with application.test_client() as c:
        yield c


def test_index(client: FlaskClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hola!!"


def test_add() -> None:
    assert add(1, 2) == 3
    assert add(1, 4) != 2
