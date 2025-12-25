from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Button:
    label: str
    click_handlers: list[ClickHandler] = field(default_factory=list)
    # 1. on_click: Callable[[Button], None] = lambda _: None

    def add_click_handler(self, handler: ClickHandler) -> None:
        self.click_handlers.append(handler)

    def click(self) -> None:
        print(f"Clicked on [{self.label}].")
        # 1. self.on_click(self)
        for handler in self.click_handlers:
            handler(self)


ClickHandler = Callable[[Button], None]


def main() -> None:
    def click_handler(button: Button) -> None:
        print(f"Handling click for button [{button.label}].")

    def another_click_handler(button: Button) -> None:
        print("I'm also handling it!")

    my_button = Button(label="Do something")
    my_button.add_click_handler(click_handler)
    my_button.add_click_handler(another_click_handler)
    # my_button = Button(label="Do something", on_click=click_handler)

    # # can use lambda function instead
    # my_button = Button(
    #     label="Do something", on_click=lambda _: print("Handling click!")
    # )
    my_button.click()


if __name__ == "__main__":
    main()
