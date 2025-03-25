from fastapi import FastAPI
from app.modules.ingredient.routes import router as ingredient_router
from app.modules.recipe.routes import router as recipe_router
from app.modules.nutrient.routes import router as nutrient_router

app = FastAPI()

prefix = "/api/v1"

app.include_router(recipe_router, prefix=prefix)
app.include_router(ingredient_router, prefix=prefix)
app.include_router(nutrient_router, prefix=prefix)