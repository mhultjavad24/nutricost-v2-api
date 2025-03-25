from pydantic import BaseModel, Field
from typing import Dict

class Recipe(BaseModel):
    name: str
    description: str
    rating: float = Field(ge=0.0, le=10.0)  # Rating between 0 and 10
    ingredients: Dict[int, float] = {}  # Dict[ingredient_id, weight_in_grams]