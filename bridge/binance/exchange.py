from abc import ABC, abstractmethod


class Exchange(ABC):
    @abstractmethod
    def get_prices(self, symbol: str) -> list[int]:
        pass

    @abstractmethod
    def buy(self, symbol: str, amount: int) -> None:
        pass

    @abstractmethod
    def sell(self, symbol: str, amount: int) -> None:
        pass
