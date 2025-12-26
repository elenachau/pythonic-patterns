from abc import ABC, abstractmethod
from visualization import Visualization


class Shape(ABC):
    @abstractmethod
    def draw(self, vis: Visualization):
        pass
