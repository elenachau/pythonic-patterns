from dataclasses import dataclass, field
from typing import Callable


def send_email(recipient: str, message: str) -> None:
    print(f"Sending email to {recipient}: '{message}'")


def send_sms(phone: str, message: str) -> None:
    print(f"Sending SMS to {phone}: '{message}'")


@dataclass
class NotificationSystem:
    recipient: str
    phone: str
    notifiers: list[Callable[[str, str], None]] = field(default_factory=list) # create callable

    def notify(self, message: str) -> None:
        for notifier in self.notifiers:
            if notifier == send_email:
                notifier(self.recipient, message)
            elif notifier == send_sms:
                notifier(self.phone, message)

    def add_notifier(self, notifier: Callable[[str, str], None]) -> None:
        self.notifiers.append(notifier)


class PaymentSystem(NotificationSystem):
    def start_maintenance(self) -> None:
        self.notify("Maintenance started")


class AuthenticationSystem(NotificationSystem):
    def clear_tokens(self) -> None:
        self.notify("Tokens cleared")


def main() -> None:
    payment_system = PaymentSystem("hi@arjancodes.com", "+31612345678")
    authentication_system = AuthenticationSystem("hi@arjancodes.com", "+31612345678")

    payment_system.add_notifier(send_email)
    payment_system.add_notifier(send_sms)
    authentication_system.add_notifier(send_email)

    payment_system.start_maintenance()
    authentication_system.clear_tokens()


if __name__ == "__main__":
    main()
