from typing import Protocol


class TradingBot(Protocol):
    def should_buy(self, symbol: str):
        """Should the bot buy the given symbol?"""

    def should_sell(self, symbol: str):
        """Should the bot sell the given symbol?"""
