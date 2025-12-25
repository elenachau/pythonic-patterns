from dataclasses import dataclass
from document import Document


@dataclass
class AppendText:
    doc: Document
    text: str

    def execute(self) -> None:
        self.doc.append(self.text)

@dataclass
class Clear:
    doc: Document

    def execute(self) -> None:
        self.doc.clear()

@dataclass
class ChangeTitle:
    doc: Document
    title: str

    def execute(self) -> None:
        self.doc.set_title(self.title)