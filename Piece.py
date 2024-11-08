from Shape import Shape
from GameNodes import GameNodes
from Node import Node
from typing import Optional, List

class Piece():
    _game_nodes: Optional[GameNodes] =  None
    _shape: Optional[Shape] = None
    _central_node: Optional[Node] = None
    _nodes: Optional[List[Node]] = None
    _shadow = None
    _t_spin = False

    def __init__(self, game_nodes: GameNodes, shape: Shape, is_secondary_spawn: bool):
        self._game_nodes = game_nodes
        self._shape = shape
        self._prepare_nodes(is_secondary_spawn)
        self._central_node = shape.coordinates[0]

    def _prepare_nodes(self, is_secondary_spawn):
        initial_node_pos = self._game_nodes.get_spawn_tile().get_position()
        if is_secondary_spawn:
            initial_node_pos = self._game_nodes.get_second_spawn_tile().get_position()
        for node_vector in range(self._shape.coordinates):
            self._game_nodes.get_node_at_position(initial_node_pos[0], node_vector[0], initial_node_pos[1], node_vector[1])
    
    def init_new_piece(self):
        for node in self._nodes:
            node.occupy(self._shape, False)
        #somethign about the shadow here

    def get_nodes(self):
        return self._nodes
    
    def destroy(self):
        for node in self._nodes:
            node.occupy(None, False)
        
    def can_move_direction(direction)