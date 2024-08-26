import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from data_for_tests import DataForTests as Dt
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


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


