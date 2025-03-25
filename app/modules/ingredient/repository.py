from typing import Dict, Optional
from .model import Ingredient

class IngredientRepository:
    def __init__(self):
        self._ingredients: Dict[int, Ingredient] = {}
        self._ingredients[1] = Ingredient(
            name="All-Purpose Flour",
            description="Standard white wheat flour for baking",
            weight_grams=1000.0
        )
        self._ingredients[2] = Ingredient(
            name="Granulated Sugar",
            description="Regular white sugar for baking and cooking",
            weight_grams=500.0
        )
        self._next_id = 3

    def get(self, ingredient_id: int) -> Optional[Ingredient]:
        return self._ingredients.get(ingredient_id)

    def create(self, ingredient: Ingredient) -> tuple[int, Ingredient]:
        ingredient_id = self._next_id
        self._ingredients[ingredient_id] = ingredient
        self._next_id += 1
        return ingredient_id, ingredient

    def update(self, ingredient_id: int, ingredient: Ingredient) -> Optional[Ingredient]:
        if ingredient_id in self._ingredients:
            self._ingredients[ingredient_id] = ingredient
            return ingredient
        return None

    def delete(self, ingredient_id: int) -> bool:
        if ingredient_id in self._ingredients:
            del self._ingredients[ingredient_id]
            return True
        return False

    def list_all(self) -> Dict[int, Ingredient]:
        return self._ingredients.copy()