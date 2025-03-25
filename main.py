from fastapi import FastAPI
from app.modules.ingredient.routes import router as ingredient_router
from app.modules.recipe.routes import router as recipe_router

app = FastAPI()

app.include_router(recipe_router, prefix="/api")
app.include_router(ingredient_router, prefix="/api")