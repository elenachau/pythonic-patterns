from bitcoin import BitcoinTradingBot
from ethereum import EthereumTradingBot
from simple_strategy import SimpleStrategy
from trading_bot import trade


def main():
    bitcoin_trader = BitcoinTradingBot()
    trade(bitcoin_trader, SimpleStrategy())

    ethereum_trader = EthereumTradingBot()
    trade(ethereum_trader, SimpleStrategy())


if __name__ == "__main__":
    main()
