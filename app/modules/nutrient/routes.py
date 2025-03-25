from fastapi import APIRouter, HTTPException
from typing import Dict, Union
from app.modules.nutrient.model import Nutrient
from app.modules.nutrient.repository import NutrientRepository

router = APIRouter()
nutrient_repository = NutrientRepository()

@router.get("/nutrients")
def list_nutrients() -> Dict[int, Nutrient]:
    return nutrient_repository.list_all()

@router.get("/nutrients/{nutrient_id}")
def read_nutrient(nutrient_id: int, q: Union[str, None] = None):
    nutrient = nutrient_repository.get(nutrient_id)
    if nutrient is None:
        raise HTTPException(status_code=404, detail="Nutrient not found")
    return nutrient

@router.post("/nutrients")
def create_nutrient(nutrient: Nutrient):
    nutrient_id, created_nutrient = nutrient_repository.create(nutrient)
    return {"nutrient_id": nutrient_id, "nutrient": created_nutrient}

@router.put("/nutrients/{nutrient_id}")
def update_nutrient(nutrient_id: int, nutrient: Nutrient):
    updated_nutrient = nutrient_repository.update(nutrient_id, nutrient)
    if updated_nutrient is None:
        raise HTTPException(status_code=404, detail="Nutrient not found")
    return updated_nutrient

@router.delete("/nutrients/{nutrient_id}")
def delete_nutrient(nutrient_id: int):
    if not nutrient_repository.delete(nutrient_id):
        raise HTTPException(status_code=404, detail="Nutrient not found")
    return {"message": "Nutrient deleted"}