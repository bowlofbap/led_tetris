import time
import constants
from Direction import Direction
from typing import Optional
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
        if not self._current_piece:
            new_piece = self._get_new_piece()
            if not new_piece:
                print("Lost Game!")
            self._bag.reset_swappable()

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
            success = self._current_piece.try_rotation_angle(direction_multiplier)
            if success:
                if self._rotations < constants.MAX_ROTATIONS:
                    self._buffer = constants.BUFFER
                    self._rotations += 1
                return True
        return False
    
    def swap_piece(self):
        new_piece_shape = self._bag.replace_swap_piece(self._current_piece)
        if new_piece_shape != self._current_piece:
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