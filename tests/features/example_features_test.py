from fastapi.testclient import TestClient
from httpx2 import Response

from server import app


def test_root() -> None:
    client = TestClient(app)
    response: Response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
