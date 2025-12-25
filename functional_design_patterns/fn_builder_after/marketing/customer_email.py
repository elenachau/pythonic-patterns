from typing import Callable
from .customer import Customer
from .email import send_email


MessageSender = Callable[[Customer, str, str], None]


def create_email_sender(
    smtp_server: str,
    smtp_port: int,
    smtp_username: str,
    smtp_password: str,
) -> MessageSender:
    def send_email_to_customer(customer: Customer, subject: str, body: str) -> None:
        send_email(
            smtp_server,
            smtp_port,
            smtp_username,
            smtp_password,
            customer.email,
            subject,
            body,
        )

    return send_email_to_customer
