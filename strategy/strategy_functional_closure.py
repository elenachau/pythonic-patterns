from dataclasses import dataclass
from typing import Callable


DiscountFunction = Callable[[int], int]


# use closures
# turn percentage_discount into a higher order function to return function that can compute discount
def percentage_discount(percentage: float) -> DiscountFunction:
    def compute_discount(price: int) -> int:
        return int(price * percentage)

    return compute_discount


def fixed_discount(price: int, fixed: int) -> int:
    return fixed


@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountFunction  # using types as abstraction (callable)

    def compute_total(self) -> int:
        discount = self.discount(self.price * self.quantity)
        return max(0, self.price * self.quantity - discount)


def main() -> None:
    order = Order(price=100_00, quantity=2, discount=percentage_discount(0.15))
    print(order)
    print(f"Total: ${order.compute_total()/100:.2f}")


if __name__ == "__main__":
    main()
