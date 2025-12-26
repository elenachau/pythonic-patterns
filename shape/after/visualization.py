from abc import ABC, abstractmethod


class Visualization(ABC):
    @abstractmethod
    def draw_poly_line(self, *args) -> None:
        pass

    @abstractmethod
    def draw_circle(self, x, y, radius) -> None:
        pass
