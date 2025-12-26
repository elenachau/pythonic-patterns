from dataclasses import dataclass
from tkinter import Canvas

from shape import Shape


@dataclass
class Circle(Shape):
    x: int
    y: int
    radius: int

    def draw(self, canvas: Canvas) -> None:
        canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
        )
