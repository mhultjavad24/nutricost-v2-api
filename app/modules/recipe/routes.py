from fastapi import APIRouter, HTTPException
from typing import Dict, Union
from app.modules.recipe.model import Recipe
from app.modules.recipe.repository import RecipeRepository
from app.modules.ingredient.repository import IngredientRepository
from app.modules.nutrient.repository import NutrientRepository

router = APIRouter()
recipe_repository = RecipeRepository()
ingredient_repository = IngredientRepository()
nutrient_repository = NutrientRepository()

@router.get("/recipes")
def list_recipes() -> Dict[int, Recipe]:
    return recipe_repository.list_all()

@router.get("/recipes/{recipe_id}")
def read_recipe(recipe_id: int, q: Union[str, None] = None):
    recipe = recipe_repository.get(recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.post("/recipes")
def create_recipe(recipe: Recipe):
    recipe_id, created_recipe = recipe_repository.create(recipe)
    return {"recipe_id": recipe_id, "recipe": created_recipe}

@router.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    if not recipe_repository.delete(recipe_id):
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted"}