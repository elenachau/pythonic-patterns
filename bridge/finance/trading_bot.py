from abc import ABC, abstractmethod
from exchange import Exchange # import abstract class

# doesn't know about CoinBase or Binance
class TradingBot(ABC):
    def __init__(self, exchange: Exchange) -> None:
        self.exchange = exchange # contains reference to Exchange ABC (the bridge)

    @abstractmethod
    def should_buy(self, symbol: str) -> bool:
        """Should the bot buy the given symbol?"""
    
    @abstractmethod
    def should_sell(self, symbol: str) -> bool:
        """Should the bot sell the given symbol?"""