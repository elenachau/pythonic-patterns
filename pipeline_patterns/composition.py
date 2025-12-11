def add_three(x: float) -> float:
    return x + 3

def multiple_by_two(x: float) -> float:
    return x * 2

def add_n(x: float, n: float) -> float:
    return x + n

def main():
    x = 12
    
    result = multiple_by_two(multiple_by_two(add_three(add_three(x)))) # not readable
    print(result)

if __name__ == "__main__":
    main()