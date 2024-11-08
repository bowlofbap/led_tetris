from typing import Optional, List
from Shape import Shape
import random

class Bag:
    _current_pieces: List[Optional[Shape]] = []
    _held_piece_shape: Optional[Shape] = None
    _can_swap = True

    def __init__(self):
        self._add_another_bag()

    def _add_another_bag(self):
        temp_bag = list(Shape)
        random.shuffle(temp_bag)
        for piece in temp_bag:
            self._current_pieces.append(piece)

    def replace_swap_piece(self, new_piece_shape):
        if not self._can_swap: return False
        origina_bag_piece = self._held_piece_shape
        self._held_piece_shape = new_piece_shape
        self._can_swap = False
        return origina_bag_piece
    
    def reset_swappable(self):
        self._can_swap = True
    
    def get_next_piece(self):
        if len(self._current_pieces < 7):
            self._add_another_bag()
        next_piece = self._current_pieces.pop(0)
        return next_piece