import math
from dataclasses import dataclass
from tkinter import Canvas

from shape import Shape


@dataclass
class Star(Shape):
    x: int
    y: int
    width: int
    height: int

    def draw(self, canvas: Canvas) -> None:
        n_points = 5
        pts = []
        rx = self.width / 2
        ry = self.height / 2
        cx = self.x + rx
        cy = self.y + ry
        theta = -math.pi / 2
        dtheta = 4 * math.pi / n_points

        for _ in range(0, n_points + 1):
            pts.append(int(round(cx + rx * math.cos(theta))))
            pts.append(int(round(cy + ry * math.sin(theta))))
            theta += dtheta

        canvas.create_line(*pts)
