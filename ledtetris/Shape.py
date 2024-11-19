from enum import Enum
from .Color import Color

class Shape(Enum):
    O = ([(0, 0), (-1, 0), (0, -1), (-1, -1)], Color.YELLOW,
         [
             [0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0],
         ])
    L = ([(0, 0), (-1, 0), (1, 0), (1, 1)], Color.RED,
         [
             [0, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 0, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 0],
         ])
    J = ([(0, 0), (-1, 0), (1, 0), (-1, 1)], Color.BLUE,
         [
             [0, 0, 0, 1, 1, 0],
             [0, 0, 0, 1, 1, 0],
             [0, 0, 0, 1, 1, 0],
             [0, 0, 0, 1, 1, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 0],
         ])
    I = ([(-1, 0), (0, 0), (1, 0), (-2, 0)], Color.CYAN,
         [
             [0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0],
         ])
    T = ([(0, 0), (-1, 0), (1, 0), (0, 1)], Color.GREEN,
         [
             [0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1],
             [0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0],
         ])
    S = ([(0, 0), (-1, 0), (0, 1), (1, 1)], Color.ORANGE,
         [
             [0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 1],
             [0, 0, 1, 1, 1, 1],
             [1, 1, 1, 1, 0, 0],
             [1, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0],
         ])
    Z = ([(0, 0), (0, 1), (-1, 1), (1, 0)], Color.MAGENTA,
         [
             [0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 0],
             [1, 1, 1, 1, 0, 0],
             [0, 0, 1, 1, 1, 1],
             [0, 0, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 0],
         ])
    X = ([(0, 0), (0, 0), (0, 0), (0, 0)], Color.GRAY,
         [
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
         ])


    @property
    def coordinates(self):
        return self.value[0]

    @property
    def color(self):
        return self.value[1]

    @property
    def bit_map(self):
        return self.value[2]