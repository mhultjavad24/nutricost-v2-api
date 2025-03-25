from pydantic import BaseModel, Field

class Nutrient(BaseModel):
    name: str
    kcal: float = Field(ge=0.0)
    fat: float = Field(ge=0.0)
    carbs: float = Field(ge=0.0)
    protein: float = Field(ge=0.0)