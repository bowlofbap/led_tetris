import time
import constants

class TetrisGame:
    _left_hold = False
    _right_hold = False
    _left_delay = time.time()
    _right_delay = time.time()
    _hold_delay = constants.HOLD_DELAY
    _hold_interval = constants.HOLD_INTERVAL
    _next_hold_tick = time.time()
    _buffer = constants.BUFFER
    _current_tetra = None
    _bag = None
    _is_running = True
    _quickdrop = False

    _speed = constants.INITIAL_SPEED
    _lines_cleared = 0
    _level = 0
    _score = 0
    _combo = 0
    _back_to_back = False

    def restart(self):
        self._current_tetra = None
        self._left_hold = False
        self._right_hold = False
        self._quickdrop = False 
        self._current_tetra = None
        self._bag = None
        self._is_running = False
        self._reset_stats()
        self.run()
    
    def run(self):
        #movement logic
        tick = time.time()
        if tick >= self._next_hold_tick:
            if self._left_hold and tick >= self._left_delay:
                print("Moving piece left")
                self._next_hold_tick = time.time() + self._hold_interval
            elif self._right_hold and tick >= self._right_delay:
                print("Moving piece right")
                self._next_hold_tick = time.time() + self._hold_interval

    def move_piece(self, direction):
        direction_xy = constants.DIRECTIONS.get(direction)
        #if self._current_tetra and constants.DIRECTIONS.get(direction):
            #success = self._current_tetra.try_move(direction)
        print(direction, direction_xy)

    def _reset_stats(self):
        self._speed = constants.INITIAL_SPEED
        self._lines_cleared = 0
        self._level = 0
        self._score = 0
        self._combo = 0
        self._back_to_back = False

    def _press_down_direction(self, direction):
        self.move_piece(direction)
        if direction == "left":
            self._left_hold = True
            self._left_delay = time.time() + self._hold_delay
        elif direction == "right":
            self._right_hold = True
            self._right_delay = time.time() + self._hold_delay

    def _release_direction(self, direction):
        print(direction + " released")
        if direction == "left":
            self._left_hold = False
        elif direction == "right":
            self._right_hold = False