from marketing.customer import Customer, CustomerType
from marketing.welcome_msg import send_welcome_message

def main() -> None:
    arjan = Customer("Arjan", "hi@arjancodes.com", CustomerType.GOLD)
    send_welcome_message(arjan)

if __name__ == "__main__":
    main()