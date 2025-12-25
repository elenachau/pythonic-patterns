from .customer import Customer, CustomerType
from .email import send_email

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "hi@arjancodes.com"
SMTP_PASSWORD = "password"


def send_welcome_message(customer: Customer) -> None:
    if customer.type == CustomerType.BRONZE:
        body = "Welcome to the Bronze plan!"
    elif customer.type == CustomerType.SILVER:
        body = "Welcome to the Silver plan!"
    elif customer.type == CustomerType.GOLD:
        body = "Welcome to the Gold plan!"
    else:
        raise ValueError(f"Unknown customer type: {customer.type}")

    send_email(
        SMTP_SERVER,
        SMTP_PORT,
        SMTP_USERNAME,
        SMTP_PASSWORD,
        customer.email,
        subject="Welcome to Arjan Codes!",
        body=body,
    )
