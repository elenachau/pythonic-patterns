from dataclasses import dataclass, field
from visualization import Visualization

@dataclass
class SvgVisualization(Visualization):
    shapes: list[str] = field(default_factory=list)

    def draw_poly_line(self, *args) -> None:
        self.shapes.append(
            f'<polyline points="{",".join(str(x) for x in args)}" style="fill:none;stroke:black;stroke-width:1" />'
        )
    
    def draw_circle(self, x, y, radius) -> None:
        self.shapes.append(
            f'<circle cx="{x}" cy="{y}" r="{radius}" stroke-width="1" fill="none" stroke="black" />'
        )
    
    def to_string(self) -> str:
        header = """<?xml version="1.0" standalone="no"?>
            <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
            "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg xmlns="http://www.w3.org/2000/svg" version="1.1">"""
        footer = "</svg>"
        return f'{header}\n{"".join(self.shapes)}\n{footer}'