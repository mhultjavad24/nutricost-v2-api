from main import app
from fastapi.testclient import TestClient
from app.modules.ingredient.model import Ingredient

client = TestClient(app)

def test_list_ingredients():
    response = client.get("/api/v1/ingredients")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()) >= 2

def test_get_ingredient():
    response = client.get("/api/v1/ingredients/1")
    assert response.status_code == 200
    assert response.json()["name"] == "All-Purpose Flour"
    
    response = client.get("/api/v1/ingredients/999")
    assert response.status_code == 404

def test_create_ingredient():
    new_ingredient = {
        "name": "Test Ingredient",
        "description": "A test ingredient",
        "weight_grams": 500.0,
        "nutrient_id": 1
    }
    response = client.post("/api/v1/ingredients", json=new_ingredient)
    assert response.status_code == 200
    assert "ingredient_id" in response.json()
    assert response.json()["ingredient"]["name"] == "Test Ingredient"

def test_create_ingredient_invalid_weight():
    new_ingredient = {
        "name": "Invalid Ingredient",
        "description": "Ingredient with invalid weight",
        "weight_grams": -100.0,
        "nutrient_id": 1
    }
    response = client.post("/api/v1/ingredients", json=new_ingredient)
    assert response.status_code == 422

def test_create_ingredient_invalid_nutrient():
    new_ingredient = {
        "name": "Invalid Ingredient",
        "description": "Ingredient with non-existent nutrient",
        "weight_grams": 100.0,
        "nutrient_id": 999
    }
    response = client.post("/api/v1/ingredients", json=new_ingredient)
    assert response.status_code == 404

def test_update_ingredient():
    updated_data = {
        "name": "Updated Flour",
        "description": "Updated flour description",
        "weight_grams": 2000.0,
        "nutrient_id": 1
    }
    response = client.put("/api/v1/ingredients/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Flour"

def test_delete_ingredient():
    new_ingredient = {
        "name": "Ingredient to Delete",
        "description": "This ingredient will be deleted",
        "weight_grams": 100.0,
        "nutrient_id": 1
    }
    create_response = client.post("/api/v1/ingredients", json=new_ingredient)
    ingredient_id = create_response.json()["ingredient_id"]
    
    response = client.delete(f"/api/v1/ingredients/{ingredient_id}")
    assert response.status_code == 200
    
    get_response = client.get(f"/api/v1/ingredients/{ingredient_id}")
    assert get_response.status_code == 404