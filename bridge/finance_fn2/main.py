from avg_trading_bot import should_buy_avg, should_sell_avg
from trading import run_bot
from binance import Binance


def main() -> None:
    # symbol we trade on
    symbol = "BTC/USD"
    trade_amount = 10

    exchange = Binance()

    run_bot(
        exchange.get_prices,
        should_buy_avg,
        should_sell_avg,
        exchange.buy,
        exchange.sell,
        symbol,
        trade_amount,
    )


if __name__ == "__main__":
    main()

