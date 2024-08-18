import random


class DataForTests:
    available_bun_names = ["black bun", "white bun", "red bun"]
    available_sauce_names = ["hot sauce", "sour cream", "chili sauce"]
    available_filling_names = ["cutlet", "dinosaur", "sausage"]
    available_ingredient_names = available_sauce_names + available_filling_names

    random_sauce = random.choice(available_sauce_names)
    random_bun = random.choice(available_bun_names)
    random_filling = random.choice(available_filling_names)

    @staticmethod
    def expected_receipt(bun_name, sauce, filling1, filling2, price):
        receipt = [
            f"(==== {bun_name} ====)",
            f"= sauce {sauce} =",
            f"= filling {filling1} =",
            f"= filling {filling2} =",
            f"(==== {bun_name} ====)\n",
            f"Price: {price}"
        ]

        return "\n".join(receipt)

