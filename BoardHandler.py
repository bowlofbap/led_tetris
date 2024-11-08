from TetrisGame import TetrisGame
from typing import Optional
from Node import Node
from Color import Color
import constants

class BoardHandler:
    _pixels      = None

    _game: Optional[TetrisGame] = None

    def __init__(self, game):
        self._game = game
        if constants.PI:
            import neopixel, board
            pixel_pin = board.D18
            num_pixels = constants.WIDTH * constants.HEIGHT
            order = neopixel.GRB
            self._pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=constants.LED_BRIGHTNESS, auto_write=False,pixel_order=order)

    def _draw_pixel(self, x, y, color: Color):
        if (x>=0 and y>=0):
            self._pixels[self._get_pixel_from_grid(x,y)] = color._value_

    #helper to translate the continuous strip into a grid
    #works for following setup

    # 9  10 11
    # 8  7  6
    # 3  4  5
    # 2  1  0

    def _get_pixel_from_grid(self, x, y):
        if (x%2 == 0):
            y = constants.HEIGHT - y - 1
        return constants.HEIGHT*(constants.WIDTH - x - 1) + y

    #blank the screen
    def clear(self):
        self._pixels.fill((0,0,0))

    #update the leds/pixels
    def _update_screen(self):
        game_nodes = self._game.get_game_nodes().get_nodes()
        for y in range(len(game_nodes)):
            for x in range(len(game_nodes[y])):
                node: Node = game_nodes[y][x]
                node_shape = node.get_shape()
                if node_shape:
                    self._draw_pixel(y, x, node_shape.color)
        self._pixels.show()

    #main update that gets called during the loop to update the screen
    def update(self):
        self.clear()
        self._update_screen()
