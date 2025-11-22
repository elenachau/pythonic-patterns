from dataclasses import dataclass


@dataclass
class Order:
    price: int
    quantity: int

    # issue is too many if-else statements, hard to extend
    def compute_total(self, discount_type: str) -> int:
        if discount_type == "percentage":
            discount = int(self.price * self.quantity * 0.20) # issue is fixed numbers
        elif discount_type == "fixed":
            discount = 10_00 # issue is fixed numbers
        else:
            discount = 0
        return max(0, self.price * self.quantity - discount)


def main() -> None:
    order = Order(price=100_00, quantity=2)
    print(order)
    print(f"Total: ${order.compute_total('percentage')/100:.2f}")


if __name__ == "__main__":
    main()
