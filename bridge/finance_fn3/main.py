from avg_trading_bot import should_buy_avg, should_sell_avg
from trading import run_bot
from binance import get_prices, buy, sell
from functools import partial


def main() -> None:
    # symbol we trade on
    symbol = "BTC/USD"
    trade_amount = 10

    should_buy = partial(should_buy_avg, symbol=symbol, get_prices=get_prices)
    should_sell = partial(should_sell_avg, symbol=symbol, get_prices=get_prices)
    buy_fn = partial(buy, symbol=symbol, amount=trade_amount)
    sell_fn = partial(sell, symbol=symbol, amount=trade_amount)

    run_bot(
        should_buy,
        should_sell,
        buy_fn,
        sell_fn,
    )


if __name__ == "__main__":
    main()
