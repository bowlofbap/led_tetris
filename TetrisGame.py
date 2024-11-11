import time
import constants
from Direction import Direction
from typing import Optional, List
from Bag import Bag
from Piece import Piece
from GameNodes import GameNodes

class TetrisGame:

    def __init__(self):
        self._left_hold = False
        self._right_hold = False
        self._left_delay = time.time()
        self._right_delay = time.time()
        self._hold_delay = constants.HOLD_DELAY
        self._hold_interval = constants.HOLD_INTERVAL
        self._next_hold_tick = time.time()
        self._buffer = constants.BUFFER
        self._current_piece: Optional[Piece] = None
        self._game_nodes: Optional[GameNodes] = None
        self._bag: Optional[Bag] = None
        self._is_running = True
        self._quickdrop = False
        self._next_frame = time.time()
        self._harddrop = False

        self._speed = constants.INITIAL_SPEED
        self._lines_cleared = 0
        self._level = 0
        self._score = 0
        self._combo = 0
        self._rotations = 0
        self._back_to_back = False
        self.restart()

    def restart(self):
        self._bag = Bag()
        self._game_nodes = GameNodes()
        self._current_piece = None
        self._left_hold = False
        self._right_hold = False
        self._quickdrop = False 
        self._current_piece = None
        self._is_running = False
        self._reset_stats()
    
    def run(self):
        #movement logic
        tick = time.time()
        if tick >= self._next_hold_tick:
            if self._left_hold and tick >= self._left_delay:
                self.move_piece(Direction.LEFT.name)
                self._next_hold_tick = time.time() + self._hold_interval
            elif self._right_hold and tick >= self._right_delay:
                self.move_piece(Direction.RIGHT.name)
                self._next_hold_tick = time.time() + self._hold_interval

        #dropping logic
        if tick >= self._next_frame or self._quickdrop:
            self._next_frame = time.time() + (self._speed - (0.47 * self._level / constants.MAX_LEVEL))
            if not self.move_piece(Direction.DOWN.name):
                if self._buffer <= 0 or not self._current_piece:
                    if self._harddrop:
                        print("HardDrop")
                    else:
                        print("SoftDrop")
                    self._harddrop = False
                    if self._current_piece: 
                        self._current_piece.solidify()
                    self.check_lines(self._current_piece)
                    self._current_piece = None
                    if not self._get_new_piece():
                        print("Lost Game!")
                    self._bag.reset_swappable()
                else:
                    self._quickdrop = False
                    self._buffer -= 1
                    self._next_frame = time.time()
            else:
                self.add_score(1)

    def check_lines(self, piece: Piece):
        added_score = 0
        self._current_piece = None
        if not piece: return 
        lines_to_clear: List[int] = []
        lines_to_check: List[int] = []

        #setting up lines to search
        for node in piece.get_nodes():
            node_y_pos = node.get_position()[1]
            if not node_y_pos in lines_to_check:
                lines_to_check.append(node_y_pos)

        #searching through each line to see if clearable
        for line_number in lines_to_check:
            clearing = True
            for x in range(constants.WIDTH):
                if not self._game_nodes.get_node_at_position(x, line_number).is_occupied():
                    clearing = False
                    break
            if clearing:
                lines_to_clear.append(line_number)
        
        #exit if nothing to be cleared
        if len(lines_to_clear) == 0:
            self._combo = 0
            return
    
        #TODO: maybe have an animation here
        for y in lines_to_clear:
            for x in range(constants.WIDTH):
                node = self._game_nodes.get_node_at_position(x, y)
                if node:
                    node.occupy(None, False)

        t_spin = piece.t_spin
        piece_shape = piece.get_shape()
        if t_spin:
            if len(lines_to_clear) == 1:
                print(piece_shape.name + "-Spin Single!")
            elif len(lines_to_clear) == 1:
                print(piece_shape.name + "-Spin Double!")
            elif len(lines_to_clear) == 1:
                print(piece_shape.name + "-Spin Triple!")

        multiplier = 0
        if len(lines_to_clear) == 1:
            if t_spin:
                multiplier = 800
            else:
                multiplier = 100
        elif len(lines_to_clear) == 2:
            if t_spin:
                multiplier = 1200
            else:
                multiplier = 300
        elif len(lines_to_clear) == 3:
            if t_spin:
                multiplier = 1600
            else:
                multiplier = 300
        elif len(lines_to_clear) == 4:
            multiplier = 800

        added_score = added_score + multiplier * self._level

        #TODO: back to back logic

        #TODO: Fix this 
        lines_to_clear.sort(reverse=True)
        print(lines_to_clear)
        for y_start in lines_to_clear:
            for y in range(y_start, constants.HEIGHT):
                for x in range(constants.WIDTH):
                    current_node_vector = (x, y)
                    new_node_vector = (x, y+1)
                    current_node = self._game_nodes.get_node_at_position(current_node_vector[0], current_node_vector[1])
                    new_node = self._game_nodes.get_node_at_position(new_node_vector[0], new_node_vector[1])
                    if new_node and current_node:
                        current_node.occupy(new_node.get_shape(), False)


        #TODO combo logic

        #TODO level up logic
    def add_score(self, score_added):
        self._score += score_added
        #TODO: display this maybe?
        print("SCORE: ", self._score)

    def set_quick_drop(self, quick_drop):
        self._quickdrop = quick_drop

    def fast_drop(self):
        added_score = 0
        while self._current_piece and self._current_piece.try_move_direction(Direction.DOWN.name):
            added_score += 2
        self.add_score(added_score)
        self._buffer = 0
        self._harddrop = True
        self._next_frame = time.time()

    def _get_new_piece(self, next_piece_shape=None):
        self._buffer = constants.BUFFER
        self._rotations = 0
        if not self._current_piece:
            if not next_piece_shape:
                next_piece_shape = self._bag.get_next_piece()
            new_piece = Piece(self._game_nodes, next_piece_shape, False)
            for node in new_piece.get_nodes():
                if node.is_occupied():
                    new_piece.init_new_piece()
                    return None
            new_piece.init_new_piece()
            self._current_piece = new_piece
            return new_piece
        return None

    def move_piece(self, direction):
        if self._current_piece:
            success = self._current_piece.try_move_direction(direction)
            return success
        return False
    
    def rotate_piece(self, direction_multiplier):
        if self._current_piece:
            success = self._current_piece.try_rotation_angle(direction_multiplier) if direction_multiplier != 2 else self._current_piece.try_rotate_180()
            if success:
                if self._rotations < constants.MAX_ROTATIONS:
                    self._buffer = constants.BUFFER
                    self._rotations += 1
                return True
        return False
    
    def swap_piece(self):
        new_piece_shape = self._bag.replace_swap_piece(self._current_piece._shape)
        #current_shape = self._current_piece.get_shape() only needed up to update the bag graphic
        if new_piece_shape != self._current_piece:
            if new_piece_shape:
                print(new_piece_shape)
            self._current_piece.destroy()
            self._current_piece = None
            self._get_new_piece(new_piece_shape)
            #update bag graphic if you have this
            #update movement tick?? maybe

    def press_down_direction(self, direction):
        self.move_piece(direction)
        if direction == Direction.LEFT.name:
            self._left_hold = True
            self._left_delay = time.time() + self._hold_delay
        elif direction == Direction.RIGHT.name:
            self._right_hold = True
            self._right_delay = time.time() + self._hold_delay

    def _reset_holds(self):
        self._left_hold = False
        self._right_hold = False
        self._quickdrop = False

    def release_direction(self, direction):
        self._reset_holds()

    def get_game_nodes(self):
        return self._game_nodes

    def _reset_stats(self):
        self._speed = constants.INITIAL_SPEED
        self._lines_cleared = 0
        self._level = 0
        self._score = 0
        self._combo = 0
        self._back_to_back = False