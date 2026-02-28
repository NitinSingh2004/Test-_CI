import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from run import app

client = TestClient(app)


def test_sum():
    response = client.post("/test", json={"a": 5, "b": 3})
    assert response.status_code == 200
