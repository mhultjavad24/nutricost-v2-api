from pydantic import BaseModel, Field

class Ingredient(BaseModel):
    name: str
    description: str
    weight_grams: float = Field(gt=0.0)  # Weight must be positive
    nutrient_id: int