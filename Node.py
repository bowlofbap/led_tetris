from Shape import Shape

class Node:
    _occupied = False
    _tetraShape = None
    _x = 0
    _y = 0
    
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def is_occupied(self):
        return self._occupied
    
    def get_position(self):
        return (self._x, self._y)
    
    def occupy(self, shape, shadow):
        if shape:
            if shape == Shape.X:
                self._occupied = True
                self._tetraShape = shape
                return
            if not shadow:
                self._occupied = True
                self._tetraShape = shape
            else:
                self._occupied = False
        else:
            self._occupied = False
            self._tetraShape = None

    def equals(self, node1, node2):
        return node1.x == node2.x and node1.y == node2.y