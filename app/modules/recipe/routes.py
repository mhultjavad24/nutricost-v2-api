from fastapi import APIRouter, HTTPException
from typing import Dict, Union
from app.modules.recipe.model import Recipe
from app.modules.recipe.repository import RecipeRepository

router = APIRouter()
recipe_repository = RecipeRepository()

@router.get("/")
def read_root():
    return {"message": "Recipe API"}

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

@router.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe: Recipe):
    updated_recipe = recipe_repository.update(recipe_id, recipe)
    if updated_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return updated_recipe

@router.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    if not recipe_repository.delete(recipe_id):
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted"}