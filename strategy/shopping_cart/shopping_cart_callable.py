from enum import StrEnum, auto
from typing import Callable


class ShippingType(StrEnum):
    STANDARD = auto()
    EXPRESS = auto()
    OVERNIGHT = auto()


ShippingFn = Callable[[str, float], float]


def standard_shipping(name: str, price: float) -> float:
    if price < 50_00:
        return 5_00
    else:
        return 0


def express_shipping(name: str, price: float) -> float:
    if price < 50_00:
        return 10_00
    else:
        return 5_00


def overnight_shipping(name: str, price: float) -> float:
    return 50_00


SHIPPING_TYPE: dict[ShippingType, ShippingFn] = {
    ShippingType.STANDARD: standard_shipping,
    ShippingType.EXPRESS: express_shipping,
    ShippingType.OVERNIGHT: overnight_shipping,
}


def get_shipping(name: str, price: float, ship_type: ShippingType) -> float:
    return SHIPPING_TYPE[ship_type](name, price)


def main() -> None:
    print(get_shipping("laptop", 150000, ShippingType.EXPRESS))
    print(get_shipping("mouse", 3000, ShippingType.EXPRESS))
    print(get_shipping("keyboard", 4000, ShippingType.OVERNIGHT))


if __name__ == "__main__":
    main()
