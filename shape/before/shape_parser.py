import json

from circle import Circle
from rectangle import Rectangle
from shape import Shape
from star import Star


def parse_shapes(filename: str) -> list[Shape]:
    with open(filename, encoding="utf8") as json_file:
        data = json.load(json_file)
        shapes: list[Shape] = []
        for shape_def in data:
            if shape_def["type"] == "circle":
                shapes.append(
                    Circle(shape_def["x"], shape_def["y"], shape_def["radius"])
                )
            elif shape_def["type"] == "rectangle":
                shapes.append(
                    Rectangle(
                        shape_def["x"],
                        shape_def["y"],
                        shape_def["width"],
                        shape_def["height"],
                    )
                )
            elif shape_def["type"] == "star":
                shapes.append(
                    Star(
                        shape_def["x"],
                        shape_def["y"],
                        shape_def["width"],
                        shape_def["height"],
                    )
                )
        return shapes
