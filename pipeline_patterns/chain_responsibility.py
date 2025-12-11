from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


# references next handler, not every handler needs to have a next handler
class Handler(ABC):
    def __init__(self) -> None:
        self.next: Optional[Handler] = None

    # typing issue because using Handler class in definition of Handler class itself, so put "Handler"
    # to directly use Handler in its own definition without quotes
    def set_next(self, handler: Handler) -> None:
        self.next = handler

    # process request to send to next handler if exists
    def handle_click_event(self) -> None:
        if self.on_click() and self.next:
            self.next.handle_click_event()  # propagates events in chain of responsibility

    # indicate whether want event to propagate
    @abstractmethod
    def on_click(self) -> bool:
        """Handle a click."""


class Button(Handler):
    def __init__(self, name: str = "Button", disabled: bool = False) -> None:
        super().__init__()  # don't use dataclass because want to call superclass; ensures self.next exists
        self.name = name
        self.disabled = disabled

    def on_click(self) -> bool:
        if self.disabled:
            return True
        print(f"Button {self.name} was clicked.")
        return False


class Panel(Handler):
    def __init__(self, name: str = "panel", disabled: bool = False) -> None:
        super().__init__()
        self.name = name
        self.disabled = disabled

    def on_click(self) -> bool:
        print(f"Panel {self.name} was clicked.")
        return True


class Window(Handler):
    def __init__(self, name: str = "window", disabled: bool = False) -> None:
        super().__init__()
        self.name = name
        self.disabled = disabled

    def on_click(self) -> bool:
        print(f"Window {self.name} was clicked.")
        return False # handles any click


def main() -> None:
    button = Button()
    panel = Panel()
    window = Window()

    # setup the chain of responsibility
    button.set_next(panel) # button is part of panel
    panel.set_next(window) # panel is part of window

    button.disabled = True
    button.handle_click_event()


if __name__ == "__main__":
    main()
