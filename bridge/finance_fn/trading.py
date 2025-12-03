from typing import Callable


GetPricesFunction = Callable[[str], list[int]] # bridge becomes this callable

