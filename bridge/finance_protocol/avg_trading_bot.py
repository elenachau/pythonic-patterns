from dataclasses import dataclass
import statistics
from bridge.finance_classic.exchange import Exchange

@dataclass
class AverageTradingBot:
    exchange: Exchange

    def should_buy(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        list_window = prices[-3:] # magic number
        return prices[-1] < statistics.mean(list_window)

    def should_sell(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        list_window = prices[-3:]
        return prices[-1] > statistics.mean(list_window)
