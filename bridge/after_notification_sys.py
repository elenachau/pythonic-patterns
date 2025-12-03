from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Notifier(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass


@dataclass
class EmailNotifier(Notifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"Sending email to {recipient}: '{message}'")


@dataclass
class SMSNotifier(Notifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"Sending SMS to {recipient}: '{message}'")


@dataclass
class NotificationSystem:
    recipient: str
    phone: str
    notifiers: list[Notifier] = field(default_factory=list)

    def notify(self, message: str) -> None:
        for notifier in self.notifiers:
            notifier.send(self.recipient, message)

    def add_notifier(self, notifier: Notifier) -> None:
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
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()

    payment_system.add_notifier(email_notifier)
    payment_system.add_notifier(sms_notifier)
    authentication_system.add_notifier(email_notifier)

    payment_system.start_maintenance()
    authentication_system.clear_tokens()


if __name__ == "__main__":
    main()
