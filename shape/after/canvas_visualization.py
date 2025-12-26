from dataclasses import dataclass
from tkinter import Canvas
from visualization import Visualization

@dataclass
class CanvasVisualization(Visualization):
    canvas: Canvas

    def draw_poly_line(self, *args) -> None:
        self.canvas.create_line(*args)
    
    def draw_circle(self, x: int, y: int, radius: int) -> None:
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius)