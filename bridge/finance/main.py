from avg_trading_bot import AverageTradingBot
from coinbase import Coinbase
# from binance import Binance
# from minmax_trading_bot import MinMaxTradingBot


def main() -> None:
    # symbol we trade on
    symbol = "BTC/USD"
    trade_amount = 10

    # create the exchange
    exchange = Coinbase()
    # exchange = Binance()

    # create the trading bot
    trading_bot = AverageTradingBot(exchange) # where connection happens in bridge strategy
    # trading_bot = MinMaxTradingBot(exchange)

    should_buy = trading_bot.should_buy(symbol)
    should_sell = trading_bot.should_sell(symbol)

    if should_buy:
        exchange.buy(symbol, trade_amount)
    elif should_sell:
        exchange.sell(symbol, trade_amount)
    else:
        print("No action needed.")


if __name__ == "__main__":
    main()
