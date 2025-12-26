from dataclasses import dataclass
from tkinter import Canvas

from shape import Shape
from visualization import Visualization


@dataclass
class Rectangle(Shape):
    x: int
    y: int
    width: int
    height: int

    def draw(self, vis: Visualization) -> None:
        vis.draw_poly_line(
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
