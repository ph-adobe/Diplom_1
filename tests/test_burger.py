import pytest
from burger import Burger
from unittest.mock import Mock
from data_for_tests import DataForTests as Dt


class TestBurger:
    def test_init_data(self):
        burger = Burger()
        assert burger.bun == None
        assert burger.ingredients == []

    def test_set_bun(self, burger, test_bun):
        burger.set_buns(test_bun)
        assert burger.bun

    def test_add_ingredient(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, burger_with_bun_and_ingredients):
        element = burger_with_bun_and_ingredients.ingredients[1]
        burger_with_bun_and_ingredients.remove_ingredient(1)
        assert element not in burger_with_bun_and_ingredients.ingredients

    @pytest.mark.parametrize(
        "old_index, new_index",
        [
            [0, 1],
            [2, 0],
            [1, 1]
        ]
    )
    def test_move_ingredient(self, burger_with_bun_and_ingredients, old_index, new_index):
        element = burger_with_bun_and_ingredients.ingredients[old_index]
        burger_with_bun_and_ingredients.move_ingredient(old_index, new_index)
        new_element_position = burger_with_bun_and_ingredients.ingredients.index(element)
        assert new_element_position == new_index

    def test_get_price_default_values(self, burger_with_bun_and_ingredients):
        actual_sum = burger_with_bun_and_ingredients.get_price()
        assert actual_sum == 400

    @pytest.mark.parametrize(
        "bun_price, ingredient_1_price, ingredient_2_price, expected_sum",
        [
            [0, 0, 0, 0],
            [1.5, 2.5, 3.0, 8.5]
        ]
    )
    def test_get_price_zero_and_float_values(self, burger, bun_price, ingredient_1_price, ingredient_2_price, expected_sum):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = ingredient_1_price
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = ingredient_2_price

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.get_price() == expected_sum

    def test_get_receipt(self, burger, test_bun, test_ingredients):
        expected_receipt = Dt.expected_receipt(
            test_bun.get_name(),
            test_ingredients[0].get_name(),
            test_ingredients[1].get_name(),
            test_ingredients[2].get_name(),
            400
        )

        burger.set_buns(test_bun)
        for ingredient in test_ingredients:
            burger.add_ingredient(ingredient)

        assert burger.get_receipt() == expected_receipt





