from Shape import Shape
from Direction import Direction
from GameNodes import GameNodes
from Wallkick import Wallkick
from Node import Node
from typing import Optional, List

class Piece:
    def __init__(self, game_nodes: GameNodes, shape: Shape, is_secondary_spawn: bool):
        self._game_nodes = game_nodes
        self._shape = shape
        self._nodes = []  # Initialize _nodes as an instance variable
        self._rotation = 0
        self._shadow = None
        self._t_spin = False
        self._central_node = None
        self._prepare_nodes(is_secondary_spawn)

    def _prepare_nodes(self, is_secondary_spawn):
        initial_node_pos = self._game_nodes.get_spawn_tile().get_position()
        if is_secondary_spawn:
            initial_node_pos = self._game_nodes.get_second_spawn_tile().get_position()

        for node_vector in self._shape.coordinates:
            node = self._game_nodes.get_node_at_position(
                initial_node_pos[0] + node_vector[0],
                initial_node_pos[1] + node_vector[1]
            )
            self._nodes.append(node)  # Append nodes to the instance variable _nodes
        self._central_node = self._nodes[0] if self._nodes else None

    def init_new_piece(self):
        for node in self._nodes:
            node.occupy(self._shape, False)
        #somethign about the shadow here

    def get_shape(self):
        return self._shape

    def get_nodes(self):
        return self._nodes
    
    def destroy(self):
        for node in self._nodes:
            node.occupy(None, False)
        
    def try_move_direction(self, direction: Direction):
        new_nodes: Optional[List[Node]] = []
        potential_central_node: Optional[Node] = None
        for node in self._nodes:
            look_at_node = self._game_nodes.get_node_at_position(node.get_position()[0] + Direction[direction].x, node.get_position()[1] + Direction[direction].y)
            if look_at_node == None or (not self._does_contain_node(look_at_node) and look_at_node.is_occupied()):
                #can't move to that direction
                return False
            new_nodes.append(look_at_node)
            if node == self._central_node:
                potential_central_node = look_at_node
        #unoccupy old nodes
        for node in self._nodes:
            node.occupy(None, False)
        self._nodes = new_nodes
        #TODO: update shadow here
        for node in self._nodes:
            node.occupy(self._shape, False)
        self._central_node = potential_central_node
        self._t_spin = False
        return True
    
    def _does_contain_node(self, check_node):
        for node in self._nodes:
            if node.equals(node, check_node):
                return True
        return False
    
    #direction_multiplier is neg/pos depending on left or right to indicate which way to search for next position in the table
    def try_rotation_angle(self, direction_multiplier):
        if self._shape == Shape.O:
            return False
        
        desired_rotation = self.__adjust_rotation(self._rotation + direction_multiplier)
        appropriate_vectors = Wallkick.I_ROTATION_VECTORS.value if self._shape == Shape.I else Wallkick.ROTATION_VECTORS.value
        rotation_tests = appropriate_vectors[self._rotation]
        i = 0
        for rotation_test in rotation_tests:
            rotation_vector_x = rotation_test[0] - appropriate_vectors[desired_rotation][i][0]
            rotation_vector_y = rotation_test[1] - appropriate_vectors[desired_rotation][i][1]
            rotation_vector = (rotation_vector_x, rotation_vector_y)
            if self.__rotate(rotation_vector, direction_multiplier):
                def __test_t_spin():
                    filled_corners = 0
                    for _ in range(4): 
                        x = self._central_node.get_position()[0]
                        y = self._central_node.get_position()[1]
                        look_at_node = self._game_nodes.get_node_at_position(x, y)
                        if look_at_node == None or look_at_node.is_occupied():
                            filled_corners += 1
                    return filled_corners >= 3
                self._t_spin = __test_t_spin
                return True
            i+=1
        return False
    
    #TODO: fix this
    def try_rotate_180(self):
        if self._shape == Shape.O:
            return False
        desired_rotation = self.__adjust_rotation(self._rotation + 2)
        appropriate_vectors = Wallkick.I_ROTATION_VECTORS.value if self._shape == Shape.I else Wallkick.ROTATION_VECTORS.value
        rotation_tests = appropriate_vectors[self._rotation]
        i = 0
        for rotation_test in rotation_tests:
            rotation_vector_x = rotation_test[0] - appropriate_vectors[desired_rotation][i][0]
            rotation_vector_y = rotation_test[1] - appropriate_vectors[desired_rotation][i][1]
            rotation_vector = (rotation_vector_x, rotation_vector_y)
            if self.__rotate(rotation_vector, 2):
                return True
            i+=1
        return False
        
    def __rotate(self, adjustment_vector, direction_multiplier):
        new_nodes: Optional[List[Node]] = []
        potential_central_node: Optional[Node] = None
        x_0 = self._central_node.get_position()[0] + adjustment_vector[0]
        y_0 = self._central_node.get_position()[1] + adjustment_vector[1]
        for node in self._nodes:
            x_1 = node.get_position()[0] + adjustment_vector[0]
            y_1 = node.get_position()[1] + adjustment_vector[1]
            a = x_0 - x_1
            b = y_1 - y_0  
            c = direction_multiplier if direction_multiplier != 2 else 1 #180 adjustment
            x2 = x_0 + (b * direction_multiplier)
            y2 = y_0 + (a * direction_multiplier)
            look_at_node = self._game_nodes.get_node_at_position(x2, y2)
            if not look_at_node or (not self._does_contain_node(look_at_node) and look_at_node.is_occupied()):
                #can't rotate in that direction
                return False
            new_nodes.append(look_at_node)
            if node == self._central_node:
                potential_central_node = look_at_node
        for node in self._nodes:
            node.occupy(None, False)
        self._nodes = new_nodes
        #TODO: update the shadow here
        for node in self._nodes:
            node.occupy(self._shape, False)
        self._rotation = self.__adjust_rotation(self._rotation + direction_multiplier)
        self._central_node = potential_central_node
        return True
    
    def __adjust_rotation(self, r):
        if r < 0:
            r = 3
        elif r > 3:
            r = 0
        return r


    def solidify(self):
        #TODO: destroy shadow here
        for node in self._nodes:
            node.occupy(self._shape, False)