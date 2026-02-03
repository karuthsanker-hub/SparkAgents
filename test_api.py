import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_productivity_endpoint():
    response = client.get("/productivity")
    assert response.status_code == 200
    assert "productivity_score" in response.json()
    assert 0 <= response.json()["productivity_score"] <= 100
