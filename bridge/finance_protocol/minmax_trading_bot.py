from dataclasses import dataclass
from bridge.finance_classic.exchange import Exchange


@dataclass
class MinMaxTradingBot:
    exchange: Exchange

    def should_buy(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        return prices[-1] < 32_000_00

    def should_sell(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        return prices[-1] > 33_000_00
