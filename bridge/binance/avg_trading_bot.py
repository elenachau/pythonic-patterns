from trading_bot import TradingBot
import statistics


class AverageTradingBot(TradingBot):
    def should_buy(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        list_window = prices[-3:] # magic number
        return prices[-1] < statistics.mean(list_window)

    def should_sell(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        list_window = prices[-3:]
        return prices[-1] > statistics.mean(list_window)
