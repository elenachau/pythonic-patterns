import statistics
from trading import GetPricesFunction


def should_buy_avg(get_prices: GetPricesFunction, symbol: str) -> bool: # remove Exchange obj by creating GetPricesFunction callable
    prices = get_prices(symbol)
    list_window = prices[-3:]  # magic number
    return prices[-1] < statistics.mean(list_window)


def should_sell_avg(get_prices: GetPricesFunction, symbol: str) -> bool:
    prices = get_prices(symbol)
    list_window = prices[-3:]
    return prices[-1] > statistics.mean(list_window)
