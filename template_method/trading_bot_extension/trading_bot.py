import random
from typing import Protocol


class TradingEngine(Protocol):
    def buy(self, amount: int) -> None:
        """Buy some crypto currency."""
        ...

    def sell(self, amount: int) -> None:
        """Sell some crypto currency."""
        ...

    def should_buy(self, prices: list[int]) -> bool:
        """Should we buy?"""
        ...

    def should_sell(self, prices: list[int]) -> bool:
        """Should we sell?"""
        ...

    def get_price_data(self) -> list[int]:
        """Get the price data."""
        ...

    def get_amount(self) -> int:
        """Get the trading amount."""
        ...


class TradingStrategy(Protocol):
    def should_buy(self, prices: list[int]) -> bool:
        """Should the bot buy?"""
        ...

    def should_sell(self, prices: list[int]) -> bool:
        """Get the price data."""
        ...


# segregate protocols
def trade(engine: TradingEngine, strategy: TradingStrategy, amount: int) -> None:
    prices = engine.get_price_data()

    if strategy.should_buy(prices):
        engine.buy(amount)
    if strategy.should_sell(prices):
        engine.sell(amount)


def get_random_trading_amount(amount: int) -> int:
    return random.randint(amount - (amount // 2), amount + (amount // 2))
