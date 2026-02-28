from fastapi.testclient import TestClient
from run import app

client = TestClient(app)


def test_sum():
    response = client.post("/test", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert "8" in response.json()["message"]
