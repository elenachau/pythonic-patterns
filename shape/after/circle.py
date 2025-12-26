from dataclasses import dataclass
from tkinter import Canvas

from shape import Shape
from visualization import Visualization


@dataclass
class Circle(Shape):
    x: int
    y: int
    radius: int

    def draw(self, vis: Visualization) -> None:
        vis.draw_circle(self.x, self.y, self.radius)
