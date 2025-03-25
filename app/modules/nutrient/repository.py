from typing import Dict, Optional
from .model import Nutrient

class NutrientRepository:
    def __init__(self):
        self._nutrients: Dict[int, Nutrient] = {}
        self._nutrients[1] = Nutrient(
            name="Apple",
            kcal=52.0,
            fat=0.2,
            carbs=14.0,
            protein=0.3
        )
        self._next_id = 2

    def get(self, nutrient_id: int) -> Optional[Nutrient]:
        return self._nutrients.get(nutrient_id)

    def create(self, nutrient: Nutrient) -> tuple[int, Nutrient]:
        nutrient_id = self._next_id
        self._nutrients[nutrient_id] = nutrient
        self._next_id += 1
        return nutrient_id, nutrient

    def update(self, nutrient_id: int, nutrient: Nutrient) -> Optional[Nutrient]:
        if nutrient_id in self._nutrients:
            self._nutrients[nutrient_id] = nutrient
            return nutrient
        return None

    def delete(self, nutrient_id: int) -> bool:
        if nutrient_id in self._nutrients:
            del self._nutrients[nutrient_id]
            return True
        return False

    def list_all(self) -> Dict[int, Nutrient]:
        return self._nutrients.copy()