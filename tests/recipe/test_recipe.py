from main import app
from fastapi.testclient import TestClient
from app.modules.recipe.model import Recipe

client = TestClient(app)

def test_list_recipes():
    response = client.get("/api/v1/recipes")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()) >= 1

def test_get_recipe():
    response = client.get("/api/v1/recipes/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Classic Chocolate Chip Cookies"
    
    response = client.get("/api/v1/recipes/999")
    assert response.status_code == 404

def test_create_recipe():
    new_recipe = {
        "name": "Test Recipe",
        "description": "A test recipe",
        "rating": 8.5,
        "ingredients": {
            "1": 100.0,
            "2": 50.0
        }
    }
    response = client.post("/api/v1/recipes", json=new_recipe)
    assert response.status_code == 200
    assert "recipe_id" in response.json()
    assert response.json()["recipe"]["name"] == "Test Recipe"

def test_create_recipe_invalid_rating():
    new_recipe = {
        "name": "Invalid Recipe",
        "description": "Recipe with invalid rating",
        "rating": 11.0,
        "ingredients": {}
    }
    response = client.post("/api/v1/recipes", json=new_recipe)
    assert response.status_code == 422

def test_delete_recipe():
    new_recipe = {
        "name": "Recipe to Delete",
        "description": "This recipe will be deleted",
        "rating": 7.0,
        "ingredients": {}
    }
    create_response = client.post("/api/v1/recipes", json=new_recipe)
    recipe_id = create_response.json()["recipe_id"]
    
    response = client.delete(f"/api/v1/recipes/{recipe_id}")
    assert response.status_code == 200
    
    get_response = client.get(f"/api/v1/recipes/{recipe_id}")
    assert get_response.status_code == 404