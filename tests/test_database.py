from data_for_tests import DataForTests as Dt


class TestDatabase:
    def test_available_buns(self, database):
        available_buns = database.available_buns()
        available_bun_names = []
        for bun in available_buns:
            available_bun_names.append(bun.get_name())
        assert available_bun_names == Dt.available_bun_names

    def test_available_ingredients(self, database):
        available_ingredients = database.available_ingredients()
        available_ingredient_names = []
        for ingredient in available_ingredients:
            available_ingredient_names.append(ingredient.get_name())
        assert available_ingredient_names == Dt.available_ingredient_names
