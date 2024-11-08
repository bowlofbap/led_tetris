from enum import Enum
from Color import Color

class Shape(Enum):
    O = ([(0, 0), (-1, 0), (0, 1), (1, 1)], Color.YELLOW.name),
    L = ([(0, 0), (-1, 0), (0, 1), (1, 1)], Color.RED.name),
    J = ([(0, 0), (-1, 0), (0, 1), (1, 1)], Color.BLUE.name),
    I = ([(0, 0), (-1, 0), (0, 1), (1, 1)], Color.CYAN.name),
    T = ([(0, 0), (-1, 0), (0, 1), (1, 1)], Color.GREEN.name),
    S = ([(0, 0), (-1, 0), (0, 1), (1, 1)], Color.ORANGE.name),
    Z = ([(0, 0), (-1, 0), (0, 1), (1, 1)], Color.MAGENTA.name),
    X = ([(0, 0), (-1, 0), (0, 1), (1, 1)], Color.GRAY.name)

    def __init__(self, value):
        self.coordinates, self.color = value