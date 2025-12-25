from dataclasses import dataclass
from enum import Enum
from typing import Callable
from functools import partial


DiscountFunction = Callable[[int], int]


class LoyaltyProgram(Enum):
    BRONZE = 1
    SILVER = 2
    GOLD = 3


def percentage_discount(price: int, percentage: float) -> int:
    return int(price * percentage)


def fixed_discount(_: int, fixed: int) -> int:
    return fixed


def loyalty_program_convertor(loyalty: LoyaltyProgram) -> DiscountFunction:
    loyalty_percentages = {
        LoyaltyProgram.BRONZE: 0.1,
        LoyaltyProgram.SILVER: 0.15,
        LoyaltyProgram.GOLD: 0.2,
    }

    return partial(percentage_discount, percentage=loyalty_percentages[loyalty])


@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountFunction

    def compute_total(self) -> int:
        discount = self.discount(self.price * self.quantity)
        return self.price * self.quantity - discount


def main() -> None:
    loyalty = LoyaltyProgram.SILVER

    loyalty_discount = loyalty_program_convertor(loyalty)
    # loyalty_discount = partial(loyalty_program_discount, loyalty=loyalty)

    order = Order(price=100_00, quantity=2, discount=loyalty_discount)
    print(order)
    print(f"Total: ${order.compute_total()/100:.2f}")


if __name__ == "__main__":
    main()
