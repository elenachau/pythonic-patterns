from tkinter import BOTH, Canvas, Frame, Menu, Tk, filedialog

from canvas_visualization import CanvasVisualization
from shape import Shape
from shape_parser import parse_shapes
from svg_visualization import SvgVisualization
from visualization import Visualization


class ShapeDrawing(Frame):
    def __init__(self, master: Tk) -> None:
        super().__init__(master)
        self.create_ui()
        self.shapes: list[Shape] = []

    def create_ui(self) -> None:
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = Menu(menubar)
        file_menu.add_command(label="Open", command=self.on_open)
        file_menu.add_command(label="Clear", command=self.on_clear)
        file_menu.add_command(label="Export", command=self.on_export)
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        self.master.title("Shape Drawing")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)

    def on_open(self) -> None:
        file = filedialog.askopenfilename(title="Select file")

        if not file:
            return
        self.shapes = parse_shapes(file)

        self.canvas.delete("all")
        self.draw_shapes(CanvasVisualization(self.canvas))

    def on_clear(self) -> None:
        self.canvas.delete("all")
        self.shapes = []

    def on_export(self) -> None:
        file = filedialog.asksaveasfile(title="Enter file name")
        svg_visualization = SvgVisualization()
        self.draw_shapes(svg_visualization)
        file.write(svg_visualization.to_string())
        file.close()

    def draw_shapes(self, vis: Visualization):
        for shape in self.shapes:
            shape.draw(vis)
