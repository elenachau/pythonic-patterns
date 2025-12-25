from marketing.customer import Customer, CustomerType
from marketing.welcome_msg import send_welcome_message
from marketing.customer_email import create_email_sender

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "hi@arjancodes.com"
SMTP_PASSWORD = "password"


def main() -> None:
    arjan = Customer("Arjan", "hi@arjancodes.com", CustomerType.GOLD)
    email_sender = create_email_sender(
        SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD
    )
    send_welcome_message(arjan, email_sender)


if __name__ == "__main__":
    main()
