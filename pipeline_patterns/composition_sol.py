from functools import reduce, partial
from typing import Callable

# use func composition

ComposableFunction = Callable[[float], float]  # compose to sequence of func


# get list of functions, apply them as sequence of arguments
def compose(*functions: ComposableFunction) -> ComposableFunction:
    # reduce performs operation on pairs within the sequence
    # returns func that applies the two functions, which is then applied to the next pair of functions
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def add_three(x: float) -> float:
    return x + 3


def multiple_by_two(x: float) -> float:
    return x * 2


def add_n(x: float, n: float) -> float:
    return x + n


def main():
    x = 12
    my_func = compose(
        partial(add_n, n=3), # same as add_three()
        add_three,
        multiple_by_two,
        multiple_by_two
    )
    result = my_func(x)
    print(result)


if __name__ == "__main__":
    main()
