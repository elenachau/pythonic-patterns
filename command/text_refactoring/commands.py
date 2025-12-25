from typing import Callable
from document import Document

UndoFunction = Callable[[], None]
CommandFunction = Callable[[], UndoFunction]  # use partial functions


# return undo function
def append_text(doc: Document, text: str) -> UndoFunction:
    # create function closure
    def undo() -> None:
        doc.text = doc.text[: -len(text)]

    doc.append(text)
    return undo


def clear_text(doc: Document) -> UndoFunction:
    text = doc.text

    def undo() -> None:
        doc.append(text)

    doc.clear()
    return undo


def change_title(doc: Document, title: str) -> UndoFunction:
    old_title = doc.title

    def undo() -> None:
        doc.set_title(old_title)

    doc.set_title(title)
    return undo


def batch(commands: list[CommandFunction]) -> UndoFunction:
    undo_fns = [
        command() for command in commands
    ]  # runs each command in list of commands

    def undo() -> None:
        for undo_fn in reversed(undo_fns):
            undo_fn()

    return undo
