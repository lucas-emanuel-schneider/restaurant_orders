from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction # noqa: F401, E261, E501
import pytest # noqa: F401, E261, E501


# Req 2
def test_dish():
    pizza = Dish('pizza', 30.00)
    lasanha = Dish('lasanha', 10.00)
    cheese = Ingredient('queijo mussarela')
    chicken_meat = Ingredient('frango')
    pizza.add_ingredient_dependency(chicken_meat, 3)
    lasanha.add_ingredient_dependency(cheese, 5)

    with pytest.raises(TypeError):
        Dish('Picanha', 'barata')
    with pytest.raises(ValueError):
        Dish('lasanha', -1)

    assert pizza.__eq__(Dish('pizza', 30.00)) is True
    assert pizza.__eq__(lasanha) is False
    assert pizza.name == 'pizza'
    assert repr(pizza) == "Dish('pizza', R$30.00)"
    assert hash(pizza) == hash(Dish('pizza', 30.00))
    assert hash(pizza) != hash(lasanha)
    assert pizza.get_restrictions() == {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED
    }
    assert pizza.get_ingredients() == {
        Ingredient('frango')
    }
