import json
from typing import Any, Callable

from shape import Shape

ShapeParser = Callable[..., Shape]

PARSER_REGISTRY: dict[str, ShapeParser] = {}


def register(shape_type: str, parser: ShapeParser) -> None:
    PARSER_REGISTRY[shape_type] = parser


def unregister(shape_type: str) -> None:
    PARSER_REGISTRY.pop(shape_type, None)


def parse_shape(args: dict[str, Any]) -> Shape:
    args_copy = args.copy()
    shape_type = args_copy.pop("type")
    return PARSER_REGISTRY[shape_type](**args_copy)


def parse_shapes(filename: str) -> list[Shape]:
    with open(filename, encoding="utf8") as json_file:
        data = json.load(json_file)
        shapes: list[Shape] = []
        for shape_def in data:
            shapes.append(parse_shape(shape_def))
        return shapes
