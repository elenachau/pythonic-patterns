from typing import Protocol


class TradingBot(Protocol):
    def should_buy(self, symbol: str) -> bool:
        """Should the bot buy the given symbol?"""

    def should_sell(self, symbol: str) -> bool:
        """Should the bot sell the given symbol?"""
