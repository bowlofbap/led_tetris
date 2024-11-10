from Shape import Shape
from Node import Node
from typing import Optional, List
from GameNodes import GameNodes

class Shadow:
    def __init__(self, shape: Shape, game_nodes: GameNodes):
        self._shape: Shape = shape
        self._nodes: Optional[Node] = []
        self._set_nodes = []
        self._game_nodes = game_nodes
    
    def _clear_nodes(self):
        for node in self._nodes:
            node.occupy(None, False)
            
    def _does_contain_node(self, nodes, check_node):
        for node in nodes:
            if node.equals(node, check_node):
                return True
        return False

    def update(self, nodes):
        self._clear_nodes()
        self._nodes = []
        self._set_nodes = []
        i = 1
        def __digging(i):
            new_nodes = []
            for node in nodes:
                node_position = node.get_position()
                look_at_node = self._game_nodes.get_node_at_position(node_position[0], node_position[1] - i)
                if not look_at_node or (not self._does_contain_node(nodes, look_at_node) and look_at_node.is_occupied()):
                    self._nodes = self._set_nodes
                    return True
                new_nodes.append(look_at_node)
            self._set_nodes = new_nodes
            return False
        while not __digging(i):
            i+=1
            #print("not digging")
        for node in self._set_nodes:
            node.occupy(self._shape, True)
            print(node.get_position()[1])

    def destroy(self):
        self._clear_nodes()
        self._nodes = []
