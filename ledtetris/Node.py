from .Shape import Shape

class Node:
    
    def __init__(self, x, y):
        self._occupied = False
        self._shape = None
        self._shadow = False
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
                self._shape = shape
                return
            if not shadow:
                self._occupied = True
                self._shape = shape
                self._shadow = False
            else:
                self._shape = shape
                self._shadow = True
                self._occupied = False
        else:
            self._occupied = False
            self._shape = None

    def get_shape(self):
        if self._shape == None: 
            return None
        else:
            return self._shape
        
    def get_shadow(self):
        return self._shadow

    def equals(self, node1, node2):
        return node1.get_position()[0] == node2.get_position()[0] and node1.get_position()[1] == node2.get_position()[1]