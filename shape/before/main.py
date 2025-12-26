from tkinter import BOTH, Canvas, Frame, Menu, Tk, filedialog
from tkinter.messagebox import showwarning

from shape import Shape
from shape_parser import parse_shapes


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
        for shape in self.shapes:
            shape.draw(self.canvas)

    def on_clear(self) -> None:
        self.canvas.delete("all")
        self.shapes = []

    def on_export(self) -> None:
        showwarning("Exporting", "To do.")


def main():
    root = Tk()
    root.title("Shape Drawing")
    root.geometry("400x250+300+300")
    _ = ShapeDrawing(root)
    root.mainloop()


if __name__ == "__main__":
    main()
