from fastapi.testclient import TestClient

from server import app


def test_root() -> None:
    client = TestClient(app)
    assert client.get("/").status_code == 200
