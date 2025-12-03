from typing import Callable


GetPricesFunction = Callable[[str], list[int]]
DecideFunction = Callable[[], bool]
BuySellFunction = Callable[[], None]


def run_bot(
    should_buy: DecideFunction,
    should_sell: DecideFunction,
    buy: BuySellFunction,
    sell: BuySellFunction,
) -> None:
    if should_buy():
        buy()
    elif should_sell():
        sell()
    else:
        print("No action needed.")
