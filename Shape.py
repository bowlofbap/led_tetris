from enum import Enum
from Color import Color

class Shape(Enum):
    O = ([(0, 0), (-1, 0), (0, -1), (-1, -1)], Color.YELLOW)
    L = ([(0, 0), (-1, 0), (1, 0), (1, 1)], Color.RED)
    J = ([(0, 0), (-1, 0), (1, 0), (-1, 1)], Color.BLUE)
    I = ([(-1, 0), (0, 0), (1, 0), (-2, 0)], Color.CYAN)
    T = ([(0, 0), (-1, 0), (1, 0), (0, 1)], Color.GREEN)
    S = ([(0, 0), (-1, 0), (0, 1), (1, 1)], Color.ORANGE)
    Z = ([(0, 0), (0, 1), (-1, 1), (1, 0)], Color.MAGENTA)
    X = ([(0, 0), (0, 0), (0, 0), (0, 0)], Color.GRAY)


    @property
    def coordinates(self):
        return self.value[0]

    @property
    def color(self):
        return self.value[1]