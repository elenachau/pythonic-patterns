from avg_trading_bot import should_buy_avg, should_sell_avg
from coinbase import Coinbase

# from binance import Binance


def main() -> None:
    # symbol we trade on
    symbol = "BTC/USD"
    trade_amount = 10

    # create the exchange
    exchange = Coinbase()
    # exchange = Binance()

    should_buy = should_buy_avg(exchange.get_prices, symbol) # get_prices becomes higher order func instead of being called in avg_trading_bot
    should_sell = should_sell_avg(exchange.get_prices, symbol)

    if should_buy:
        exchange.buy(symbol, trade_amount)
    elif should_sell:
        exchange.sell(symbol, trade_amount)
    else:
        print("No action needed.")


if __name__ == "__main__":
    main()
