from bitcoin import BitcoinTradingEngine
from ethereum import EthereumTradingEngine
from simple_strategy import SimpleStrategy
from disable_buy_temporarily import DisableBuyTemporarilyStrategy
from trading_bot import trade, get_random_trading_amount


def main():
    bitcoin_trader = BitcoinTradingEngine()
    trade(bitcoin_trader, SimpleStrategy(), bitcoin_trader.get_amount())

    ethereum_trader = EthereumTradingEngine()
    trade(
        ethereum_trader,
        DisableBuyTemporarilyStrategy(),
        get_random_trading_amount(ethereum_trader.get_amount()),
    )

    bitcoin_trader = BitcoinTradingEngine()
    trade(bitcoin_trader, SimpleStrategy(), 100_00)


if __name__ == "__main__":
    main()
