from tkinter import Tk

from circle import Circle
from rectangle import Rectangle
from star import Star
from shape_drawing import ShapeDrawing
from shape_parser import register


def main():
    # register shape parsers
    register("circle", Circle)
    register("rectangle", Rectangle)
    register("star", Star)

    root = Tk()
    root.title("Shape Drawing")
    root.geometry("400x250+300+300")
    _ = ShapeDrawing(root)
    root.mainloop()


if __name__ == "__main__":
    main()
