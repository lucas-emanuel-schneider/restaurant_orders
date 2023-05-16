from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1.
def test_ingredient():
    chicken_meat = Ingredient('frango')
    cheese = Ingredient('queijo mussarela')
    egg = Ingredient('ovo')
    assert repr(chicken_meat) == "Ingredient('frango')"
    assert hash(chicken_meat) == hash(Ingredient('frango'))
    assert hash(cheese) != hash(egg)
    assert egg.name == 'ovo'
    assert chicken_meat.__eq__(Ingredient('frango')) is True
    assert chicken_meat.__eq__(egg) is False
    assert cheese.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }
