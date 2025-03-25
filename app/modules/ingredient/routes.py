from fastapi import APIRouter, HTTPException
from typing import Dict, Union
from app.modules.ingredient.model import Ingredient
from app.modules.ingredient.repository import IngredientRepository
from app.modules.nutrient.repository import NutrientRepository

router = APIRouter()
ingredient_repository = IngredientRepository()
nutrient_repository = NutrientRepository()

@router.get("/ingredients")
def list_ingredients() -> Dict[int, Ingredient]:
    return ingredient_repository.list_all()

@router.get("/ingredients/{ingredient_id}")
def read_ingredient(ingredient_id: int, q: Union[str, None] = None):
    ingredient = ingredient_repository.get(ingredient_id)
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

@router.post("/ingredients")
def create_ingredient(ingredient: Ingredient):
    # Validate that the nutrient exists
    if nutrient_repository.get(ingredient.nutrient_id) is None:
        raise HTTPException(status_code=404, detail="Referenced nutrient not found")
    
    ingredient_id, created_ingredient = ingredient_repository.create(ingredient)
    return {"ingredient_id": ingredient_id, "ingredient": created_ingredient}

@router.put("/ingredients/{ingredient_id}")
def update_ingredient(ingredient_id: int, ingredient: Ingredient):
    # Validate that the nutrient exists
    if nutrient_repository.get(ingredient.nutrient_id) is None:
        raise HTTPException(status_code=404, detail="Referenced nutrient not found")
    
    updated_ingredient = ingredient_repository.update(ingredient_id, ingredient)
    if updated_ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return updated_ingredient

@router.delete("/ingredients/{ingredient_id}")
def delete_ingredient(ingredient_id: int):
    if not ingredient_repository.delete(ingredient_id):
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return {"message": "Ingredient deleted"}