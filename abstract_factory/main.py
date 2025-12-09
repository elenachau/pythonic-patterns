def calculate_simple_tax(income: int) -> int:
    return int(income * 0.1)


def calculate_nl_tax(income: int, apply_floor: bool = True) -> int:
    brackets: list[tuple[int | None, float]] = [
        (69_398_00, 0.37),
        (None, 0.495),
    ]
    taxable_income = income
    if apply_floor:
        taxable_income -= 10_000_00

    total_tax = 0
    for max_income, percentage in brackets:
        bracket_income = min(taxable_income, max_income or taxable_income)
        total_tax += int(bracket_income * percentage)
        taxable_income -= bracket_income
        if taxable_income <= 0:
            break
    return total_tax


def calculate_capital_tax(capital: int) -> int:
    return int(capital * 0.5)


def compute_tax(income: int, capital: int, apply_floor: bool = True) -> int:
    has_capital_tax = True
    use_nl_income_tax = True

    # calculate the tax
    income_tax = (
        calculate_nl_tax(income, apply_floor)
        if use_nl_income_tax
        else calculate_simple_tax(income)
    )
    capital_tax = calculate_capital_tax(capital) if has_capital_tax else 0

    # return the total tax
    return income_tax + capital_tax


def main():
    # compute the tax
    income = 100_000_00
    capital = 100_000_00
    tax = compute_tax(income, capital)
    print(
        f"Tax for income ${income/100:.2f} and capital ${capital/100:.2f} is ${tax/100:.2f}."
    )


if __name__ == "__main__":
    main()
