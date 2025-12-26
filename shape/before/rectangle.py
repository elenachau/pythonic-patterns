from dataclasses import dataclass
from tkinter import Canvas

from shape import Shape


@dataclass
class Rectangle(Shape):
    x: int
    y: int
    width: int
    height: int

    def draw(self, canvas: Canvas) -> None:
        canvas.create_line(
            self.x,
            self.y,
            self.x + self.width,
            self.y,
            self.x + self.width,
            self.y + self.height,
            self.x,
            self.y + self.height,
            self.x,
            self.y,
        )
