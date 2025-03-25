from main import app
from fastapi.testclient import TestClient
from app.modules.nutrient.model import Nutrient

client = TestClient(app)

def test_list_nutrients():
    response = client.get("/api/v1/nutrients")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()) >= 1

def test_get_nutrient():
    response = client.get("/api/v1/nutrients/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Apple"
    
    response = client.get("/api/v1/nutrients/999")
    assert response.status_code == 404

def test_create_nutrient():
    new_nutrient = {
        "name": "Test Nutrient",
        "kcal": 150.0,
        "fat": 5.0,
        "carbs": 20.0,
        "protein": 8.0
    }
    response = client.post("/api/v1/nutrients", json=new_nutrient)
    assert response.status_code == 200
    assert "nutrient_id" in response.json()
    assert response.json()["nutrient"]["name"] == "Test Nutrient"

def test_create_nutrient_invalid_values():
    new_nutrient = {
        "name": "Invalid Nutrient",
        "kcal": -100.0,
        "fat": -1.0,
        "carbs": -5.0,
        "protein": -2.0
    }
    response = client.post("/api/v1/nutrients", json=new_nutrient)
    assert response.status_code == 422

def test_update_nutrient():
    updated_data = {
        "name": "Updated Apple",
        "kcal": 60.0,
        "fat": 0.3,
        "carbs": 15.0,
        "protein": 0.4
    }
    response = client.put("/api/v1/nutrients/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Apple"

def test_delete_nutrient():
    new_nutrient = {
        "name": "Nutrient to Delete",
        "kcal": 100.0,
        "fat": 2.0,
        "carbs": 10.0,
        "protein": 5.0
    }
    create_response = client.post("/api/v1/nutrients", json=new_nutrient)
    nutrient_id = create_response.json()["nutrient_id"]
    
    response = client.delete(f"/api/v1/nutrients/{nutrient_id}")
    assert response.status_code == 200
    
    get_response = client.get(f"/api/v1/nutrients/{nutrient_id}")
    assert get_response.status_code == 404