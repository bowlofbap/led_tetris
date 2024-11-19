from typing import Optional, List
from Shape import Shape
import random

class Bag:

    def __init__(self):
        self._current_pieces: List[Optional[Shape]] = []
        self._held_piece_shape: Optional[Shape] = None
        self._can_swap = True
        self._add_another_bag()

    def _add_another_bag(self):
        temp_bag = list(Shape)
        temp_bag.pop(7)
        random.shuffle(temp_bag)
        for piece in temp_bag:
            self._current_pieces.append(piece)

    def peek_swap_piece(self):
        return self._held_piece_shape

    def replace_swap_piece(self, new_piece_shape):
        if not self._can_swap: return False
        original_bag_piece = self._held_piece_shape
        self._held_piece_shape = new_piece_shape
        self._can_swap = False
        return original_bag_piece
    
    def reset_swappable(self):
        self._can_swap = True
    
    def get_next_piece(self):
        if len(self._current_pieces) < 7:
            self._add_another_bag()
        next_piece = self._current_pieces.pop(0)
        return next_piece
    
    def get_all_pieces(self):
        return self._current_pieces