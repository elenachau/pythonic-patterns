from dataclasses import dataclass
from typing import Callable


DiscountFunction = Callable[[int], int]


# # remove class because callable can be used in Order class
# class DiscountStrategy(ABC): # turns into a callable
#     def __call__(self, price: int) -> int:
#         """Compute the discount for the given price."""


@dataclass
class PercentageDiscount:  # no inheritance relationship, relies on duck typing
    percentage: float  # remove magic numbers

    def __call__(self, price: int) -> int:
        return int(price * self.percentage)


@dataclass
class FixedDiscount:
    fixed: int

    def __call__(self, price: int) -> int:
        return self.fixed


@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountFunction # using types as abstraction (callable)

    def compute_total(self) -> int:
        discount = self.discount(
            self.price * self.quantity
        )  # because discount is callable
        return max(0, self.price * self.quantity - discount)


def main() -> None:
    order = Order(price=100_00, quantity=2, discount=FixedDiscount(5_00))
    print(order)
    print(f"Total: ${order.compute_total()/100:.2f}")


if __name__ == "__main__":
    main()
