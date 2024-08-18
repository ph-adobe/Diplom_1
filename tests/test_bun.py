import pytest
from bun import Bun


class TestBun:
    def test_init__valid_data(self):
        bun = Bun("Test bun", 10)
        assert bun.name == "Test bun"
        assert bun.price == 10

    @pytest.mark.parametrize(
        "bun_name",
        ["", "a", "1111", f"b{256*'u'}n"]
    )
    def test_get_name_return_valid_name(self, bun_name):
        bun = Bun(bun_name, 10)
        name = bun.get_name()
        assert name == bun_name

    @pytest.mark.parametrize(
        "bun_price",
        [1, 0, 10, 100000000]
    )
    def test_get_price_return_valid_price(self, bun_price):
        bun = Bun("Test bun", bun_price)
        price = bun.get_price()
        assert price == bun_price

