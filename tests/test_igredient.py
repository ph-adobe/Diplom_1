import pytest
from ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_type, ingredient_name, price",
        [
            ["соус", "космический соус", 10],
            ["начинка", "космическая начинка", 100]
        ]
    )
    def test_init_data(self, ingredient_type, ingredient_name, price):
        ingredient = Ingredient(ingredient_type, ingredient_name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == ingredient_name
        assert ingredient.price == price

    @pytest.mark.parametrize(
        "price",
        [0, 100]
    )
    def test_get_price_valid_value(self, price):
        ingredient = Ingredient("test_type", "test_name", price)
        ingredient_price = ingredient.get_price()
        assert ingredient_price == price

    @pytest.mark.parametrize(
        "name",
        ["test", "", 123456, f"{256*'a'}"]
    )
    def test_get_name(self, name):
        ingredient = Ingredient("test_type", name,111)
        ingredient_name = ingredient.get_name()
        assert ingredient_name == name

    @pytest.mark.parametrize(
        "ingredient_type",
        ["соус", "начинка", "", 123456]
    )
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "name", 111)
        ingredient_type = ingredient.get_type()
        assert ingredient_type == ingredient_type
