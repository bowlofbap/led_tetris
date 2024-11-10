from Node import Node
from constants import HEIGHT, WIDTH
from typing import List, Optional

class GameNodes:

    def __init__(self):
        self._nodes: List[List[Optional[Node]]] = [[None for _ in range(HEIGHT)] for _ in range(WIDTH)]
        self._spawn_tile: Optional[Node]  = None
        self._second_spawn_tile: Optional[Node] = None
        self.reset()

    def reset(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                new_node = Node(x, y)
                self._nodes[x][y] = new_node
                if x == int(WIDTH/2) and y == HEIGHT-2:
                    self._spawn_tile = new_node
                elif x == int(WIDTH/2) and y == HEIGHT-1:
                    self._second_spawn_tile = new_node

    def clear(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                self._nodes[x][y] = None

    def get_nodes(self):
        return self._nodes
    
    def get_node_at_position(self, x, y) -> Optional[Node]:
        if x < 0 or y < 0 or x > WIDTH - 1 or y > HEIGHT - 1:
            return None
        return self._nodes[x][y]
    
    def get_spawn_tile(self):
        return self._spawn_tile
    
    def get_second_spawn_tile(self):
        return self._second_spawn_tile
