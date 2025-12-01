from abc import ABC, abstractmethod
from dataclasses import dataclass


class DiscountStrategy(ABC):
    @abstractmethod
    def compute(self, price: int) -> int:
        """Compute the discount for the given price."""

class PercentageDiscount(DiscountStrategy):
    def compute(self, price: int) -> int:
        return int(price * 0.20)
    
class FixedDiscount(DiscountStrategy):
    def compute(self, price: int) -> int:
        return 10_00 # return fixed discount value
    
# # alt: protocol removes inheritance relationship (compared to ABC)
# class DiscountStrategy(Protocol):
#     def compute(self, price: int) -> int:
#         """Compute the discount for the given price."""

# class PercentageDiscount:
#     def compute(self, price: int) -> int:
#         return int(price * 0.20)
    
# class FixedDiscount:
#     def compute(self, price: int) -> int:
#         return 10_00 # return fixed discount value


@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountStrategy # no longer have to specify discount type

    def compute_total(self) -> int:
        discount = self.discount.compute(self.price * self.quantity)
        return max(0, self.price * self.quantity - discount)


def main() -> None:
    order = Order(price=100_00, quantity=2, discount=PercentageDiscount())
    print(order)
    print(f"Total: ${order.compute_total()/100:.2f}")


if __name__ == "__main__":
    main()
