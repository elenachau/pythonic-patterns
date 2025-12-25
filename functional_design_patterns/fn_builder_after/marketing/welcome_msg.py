from typing import Callable
from .customer import Customer, CustomerType

MessageSender = Callable[[Customer, str, str], None]


def send_welcome_message(customer: Customer, sender: MessageSender) -> None:
    if customer.type == CustomerType.BRONZE:
        body = "Welcome to the Bronze plan!"
    elif customer.type == CustomerType.SILVER:
        body = "Welcome to the Silver plan!"
    elif customer.type == CustomerType.GOLD:
        body = "Welcome to the Gold plan!"
    else:
        raise ValueError(f"Unknown customer type: {customer.type}")

    sender(
        customer,
        "Welcome to Arjan Codes!",
        body,
    )
