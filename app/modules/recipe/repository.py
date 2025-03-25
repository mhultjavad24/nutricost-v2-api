from typing import Dict, Optional
from .model import Recipe

class RecipeRepository:
    def __init__(self):
        self._recipes: Dict[int, Recipe] = {}
        self._recipes[1] = Recipe(
            name="Classic Chocolate Chip Cookies",
            description="Delicious homemade chocolate chip cookies that are soft and chewy",
            rating=9.5,
            ingredients={
                1: 250.0,  # 250g of flour
                2: 200.0   # 200g of sugar
            }
        )
        self._next_id = 2

    def get(self, recipe_id: int) -> Optional[Recipe]:
        return self._recipes.get(recipe_id)

    def create(self, recipe: Recipe) -> tuple[int, Recipe]:
        recipe_id = self._next_id
        self._recipes[recipe_id] = recipe
        self._next_id += 1
        return recipe_id, recipe

    def update(self, recipe_id: int, recipe: Recipe) -> Optional[Recipe]:
        if recipe_id in self._recipes:
            self._recipes[recipe_id] = recipe
            return recipe
        return None

    def delete(self, recipe_id: int) -> bool:
        if recipe_id in self._recipes:
            del self._recipes[recipe_id]
            return True
        return False

    def list_all(self) -> Dict[int, Recipe]:
        return self._recipes.copy()