from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """
    Basic test: backend root (/) should return 200 OK.
    This satisfies Fusionpact's CI/CD 'test' requirement.
    """
    response = client.get("/")
    assert response.status_code == 200
