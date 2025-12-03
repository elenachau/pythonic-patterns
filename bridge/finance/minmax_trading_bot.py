from trading_bot import TradingBot


class MinMaxTradingBot(TradingBot):
    def should_buy(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        list_window = prices[-3:]  # magic number
        return prices[-1] < 32_000_00

    def should_sell(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        list_window = prices[-3:]
        return prices[-1] > 33_000_00
