from abc import ABC, abstractmethod


class IncomeTaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self, income: int, apply_floor: bool = True) -> int:
        """Calculates income tax."""
        ...


class SimpleIncomeTaxCalculator(IncomeTaxCalculator):
    def calculate_tax(self, income: int, apply_floor: bool = True) -> int:
        return int(income * 0.1)


class NLIncomeTaxCalculator(IncomeTaxCalculator):
    def calculate_tax(self, income: int, apply_floor: bool = True) -> int:
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


class CapitalTaxCalculator(ABC):
    @abstractmethod
    def calculate_capital_tax(self, capital: int) -> int:
        """Calculate capital tax."""
        ...


class PercentageCapitalTaxCalculator(CapitalTaxCalculator):
    def calculate_capital_tax(self, capital: int) -> int:
        return int(capital * 0.05)


class ZeroCapitalTaxCalculator(CapitalTaxCalculator):
    def calculate_capital_tax(self, capital: int) -> int:
        return 0


class TaxFactory(ABC):  # simply a class that produces other objects
    @abstractmethod
    def create_income_tax_calculator(self) -> IncomeTaxCalculator:
        """Creates an income tax calculator."""
        ...

    @abstractmethod
    def create_capital_tax_calculator(self) -> CapitalTaxCalculator:
        """Creates a capital tax calculator."""
        ...


class SimpleTaxFactory(TaxFactory):
    def create_income_tax_calculator(self) -> IncomeTaxCalculator:
        return SimpleIncomeTaxCalculator()

    def create_capital_tax_calculator(self) -> CapitalTaxCalculator:
        return ZeroCapitalTaxCalculator()


class NLTaxFactory(TaxFactory):
    def create_income_tax_calculator(self) -> IncomeTaxCalculator:
        return NLIncomeTaxCalculator()

    def create_capital_tax_calculator(self) -> CapitalTaxCalculator:
        return PercentageCapitalTaxCalculator()


def compute_tax(
    factory: TaxFactory, income: int, capital: int, apply_floor: bool = True
) -> int:

    # create the tax calculators, remove the booleans
    income_tax_calculator = factory.create_income_tax_calculator()
    capital_tax_calculator = factory.create_capital_tax_calculator()

    # calculate the tax
    income_tax = income_tax_calculator.calculate_tax(income, apply_floor)
    capital_tax = capital_tax_calculator.calculate_capital_tax(capital)

    # return the total tax
    return income_tax + capital_tax


def main():
    # create the factory
    factory = NLTaxFactory()

    # compute the tax
    income = 100_000_00
    capital = 100_000_00
    tax = compute_tax(factory, income, capital)
    print(
        f"Tax for income ${income/100:.2f} and capital ${capital/100:.2f} is ${tax/100:.2f}."
    )


if __name__ == "__main__":
    main()
