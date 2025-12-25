from dataclasses import dataclass, field
from controller import Command
from document import Document


@dataclass
class AppendText:
    doc: Document
    text: str

    def execute(self) -> None:
        self.doc.append(self.text)

    def undo(self) -> None:
        self.doc.text = self.doc.text[:-len(self.text)]

@dataclass
class Clear:
    doc: Document
    _old_text: str = ""

    def execute(self) -> None:
        self._old_text = self.doc.text
        self.doc.clear()

    def undo(self) -> None:
        self.doc.append(self._old_text)

@dataclass
class ChangeTitle:
    doc: Document
    title: str
    _old_title: str = ""

    def execute(self) -> None:
        self._old_title = self.doc.title
        self.doc.set_title(self.title)

    def undo(self) -> None:
        self.doc.set_title(self._old_title)

@dataclass
class Batch:
    commands: list[Command] = field(default_factory=list)

    def execute(self) -> None:
        for command in self.commands:
            command.execute()
    
    def undo(self) -> None:
        for command in reversed(self.commands):
            command.undo()