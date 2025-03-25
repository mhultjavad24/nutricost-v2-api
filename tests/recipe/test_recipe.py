from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_list_recipes():
    response = client.get("/api/v1/recipes")
    assert response.status_code == 200
