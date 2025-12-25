from dataclasses import dataclass
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