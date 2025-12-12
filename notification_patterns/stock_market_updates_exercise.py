from dataclasses import dataclass, field


@dataclass
class Investor:
    name: str

    def update(self, message: str) -> None:
        print(f"{self.name} received message: {message}")


@dataclass
class StockMarket:
    subscribers: dict[str, list[Investor]] = field(default_factory=dict)

    def subscribe(self, investor: Investor, company_name: str) -> None:
        if company_name not in self.subscribers:
            self.subscribers[company_name] = []
        self.subscribers[company_name].append(investor)
    
    def unsubscribe(self, investor: Investor, company_name: str) -> None:
        if investor in self.subscribers[company_name]:
            self.subscribers[company_name].remove(investor)
    
    def issue_stock(self, company_name: str, num_stocks: int) -> None:
        message = f"New stocks issued for {company_name}: {num_stocks}"
        self._notify_subscribers(company_name, message)

    def announce_earnings_report(self, company_name: str, earning_reports: str) -> None:
        message = f"New stocks issued for {company_name}: {earning_reports}"
        self._notify_subscribers(company_name, message)
    
    def _notify_subscribers(self, company_name: str, message: str) -> None:
        if company_name in self.subscribers:
            for subscriber in self.subscribers[company_name]:
                subscriber.update(message)

def main() -> None:
    # create stock market and investors
    stock_market = StockMarket()
    investor1 = Investor("Investor 1")
    investor2 = Investor("Investor 2")

    # subscribe investors to companies
    stock_market.subscribe(investor1, "Apple")
    stock_market.subscribe(investor2, "Apple")
    stock_market.subscribe(investor2, "Google")

    # issue new stocks for a company
    stock_market.issue_stock("Apple", 100)

    # announce earnings report for Google
    stock_market.announce_earnings_report(
        "Google", "Earnings report for Q4 2022: revenue $100B, profit $20B"
    )

    # unsubscribe an investor from a company
    stock_market.unsubscribe(investor2, "Apple")

    # announce earnings report for Apple
    stock_market.announce_earnings_report(
        "Apple", "Earnings report for Q4 2022: revenue $220B, profit $50B"
    )


if __name__ == "__main__":
    main()
