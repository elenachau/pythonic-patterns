from dataclasses import dataclass, field
from typing import Protocol


class Command(Protocol):
    def execute(self) -> None:
        """Execute the command."""

    def undo(self) -> None:
        """Undo the command."""

@dataclass
class TextController:
    undo_stack: list[Command] = field(default_factory=list)
    def execute(self, command: Command) -> None:
        command.execute()
        self.undo_stack.append(command)
    
    def undo(self) -> None:
        if not self.undo_stack:
            return
        command = self.undo_stack.pop()
        command.undo()

    def undo_all(self) -> None:
        while self.undo_stack:
            self.undo()