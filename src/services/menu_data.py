from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.data = pd.read_csv(source_path).itertuples(index=False)
        self.create_dishes()

    def create_dishes(self):
        for name, price, ing, qtt in self.data:
            new_dish = Dish(name, float(price))
            if new_dish not in self.dishes:
                new_dish.add_ingredient_dependency(Ingredient(ing), int(qtt))
                self.dishes.add(new_dish)
            else:
                for item in self.dishes:
                    if item == new_dish:
                        item.add_ingredient_dependency(
                            Ingredient(ing), int(qtt))
