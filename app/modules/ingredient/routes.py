from fastapi import APIRouter
from typing import Union
from app.modules.ingredient.model import Ingredient

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Ingredient API"}

@router.get("/ingredients/{ingredient_id}")
def read_ingredient(ingredient_id: int, q: Union[str, None] = None):
    return {"ingredient_id": ingredient_id, "q": q}

@router.put("/ingredients/{ingredient_id}")
def update_ingredient(ingredient_id: int, ingredient: Ingredient):
    return {"ingredient_name": ingredient.name, "ingredient_id": ingredient_id}