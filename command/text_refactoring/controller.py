from typing import Protocol


class Command(Protocol):
    def execute(self) -> None:
        """Execute the command."""


class TextController:
    def execute(self, command: Command) -> None:
        command.execute()
