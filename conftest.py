import pytest

from bun import Bun
from burger import Burger
from data_for_tests import DataForTests as Dt
from database import Database
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture(autouse=True)
def burger():
    return Burger()


@pytest.fixture()
def test_bun():
    return Bun(Dt.random_bun, 50)


@pytest.fixture()
def test_ingredients():
    ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, Dt.random_sauce, 100)
    ingredient_filling_1 = Ingredient(INGREDIENT_TYPE_FILLING, Dt.random_filling, 100)
    ingredient_filling_2 = Ingredient(INGREDIENT_TYPE_FILLING, Dt.random_filling, 100)
    return [ingredient_sauce, ingredient_filling_1, ingredient_filling_2]


@pytest.fixture()
def burger_with_bun_and_ingredients(burger, test_bun, test_ingredients):
    for ingredient in test_ingredients:
        burger.add_ingredient(ingredient)
    burger.set_buns(test_bun)
    return burger


@pytest.fixture()
def database():
    return Database()

# @pytest.fixture()
# def burger_with_bun_and_ingredients(burger):
#     mock_bun = Mock()
#     burger.set_buns(mock_bun)
#     mock_ingredient_1 = Mock()
#     mock_ingredient_2 = Mock()
#     mocks = [mock_ingredient_1, mock_ingredient_2]
#     for mock in mocks:
#         burger.add_ingredient(mock)
#     return burger, mock_bun, mock_ingredient_1, mock_ingredient_2

