from pydantic import BaseModel, Field

class Recipe(BaseModel):
    name: str
    description: str
    rating: float = Field(ge=0.0, le=10.0)  # Rating between 0 and 10