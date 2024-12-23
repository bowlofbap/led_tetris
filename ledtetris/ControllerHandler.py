from .constants import BLUETOOTH_DIRECTIONS
from .Direction import Direction
from .ControllerMap import ControllerMap
from .BoardHandler import BoardHandler
from .TetrisGame import TetrisGame
from .PreviewHandler import PreviewHandler
import pygame
import math
import sys

class ControllerHandler:
    #abstraction to handle inputs and gameloop and wraps around the game itself
    _bluetooth         = True
    _pi                = None
    _debug             = False

    def __init__(self, game, debug = False):
        self._clock             = None
        self._joystick          = None
        self._last_direction    = None
        self._running           = True
        self._game: TetrisGame  = game
        self._debug = debug
        self._board_handler = BoardHandler(game)
        self._preview_handler = PreviewHandler(game)

    #called externally to kick off listening for inputs
    def start(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        pygame.joystick.init()
        joystick_detected = False
        while joystick_detected==False:
            print("Waiting for controller...")
            pygame.joystick.quit()
            pygame.joystick.init()
            try:
                joystick = pygame.joystick.Joystick(0) # create a joystick instance
                joystick.init() # init instance
                self._joystick = joystick
                joystick_detected = True
                print("controller found")
            except pygame.error:
                print("not enough joystick found.")
                self._preview_handler.show_text("Waiting for controller...")
                joystick_detected = False
        self.loop()

    def loop(self):
        while self._running:
            if not self._debug:
                #change this to a public method, not using private 
                for event in pygame.event.get():
                    if event.type == pygame.JOYAXISMOTION:
                        axis = event.axis         # Axis number (0 for horizontal, 1 for vertical)
                        position = event.value    # Position on the axis (-1.0 to 1.0)
                        direction, motion = self._convert_bt_to_direction_and_motion(axis, position)
                        if motion == "press":
                            self._process_direction_down(direction)
                        elif motion == "release":
                            self._process_direction_up(direction)
                    elif event.type == pygame.JOYBUTTONDOWN:
                        button = event.button        
                        self._process_button_down(button)
                    elif event.type == pygame.JOYBUTTONUP:
                        button = event.button        
                        self._process_button_up(button)
                self._game.run()
            if not self._game._is_running:
                self._game.restart()
            self._board_handler.update()
            self._preview_handler.update()
            self._clock.tick(30)
        self.clear_screen()
        pygame.quit()
        sys.exit()

    def _process_direction_down(self, input):
        if input == Direction.LEFT.name or input == Direction.RIGHT.name:
            self._game.press_down_direction(input)
        elif input == Direction.DOWN.name:
            self._game.set_quick_drop(True)
        elif input == Direction.UP.name:
            self._game.fast_drop()

    def _process_direction_up(self, input):
        self._game.release_direction(input)

    def _process_button_down(self, input):
        if input == ControllerMap.L.value:
            self._game.rotate_piece(-1)
        elif input == ControllerMap.R.value:
            self._game.rotate_piece(1)
        elif input == ControllerMap.Y.value:
            #self._game.rotate_piece(2)
            print("180 turn not implemented yet")
        elif input == ControllerMap.START.value:
            self._running = False
        elif input == ControllerMap.SELECT.value:
            self._game.restart()
        elif input == ControllerMap.X.value:
            self._game.swap_piece()

    def clear_screen(self):
        self._board_handler.turn_off()
        self._preview_handler.clear()

    def _process_button_up(self, input):
        input

    def _convert_bt_to_direction_and_motion(self, raw_input_x, raw_input_y):
        # Handle release state
        if abs(raw_input_y) <= 0.1:
            # Return the last known direction for button release
            #potentially throwing error somehow if up is handled before a down press? maybe throw
            released_direction = self._last_direction
            self._last_direction = None  # Reset after handling release
            return released_direction, "release"

        # Calculate which direction matches the input for button down presses
        closest_direction = None
        smallest_distance = float('inf')
        
        for direction, vector in BLUETOOTH_DIRECTIONS.items():
            # Calculate Euclidean distance between input and direction vector
            distance = math.sqrt((raw_input_x - vector['x']) ** 2 + (raw_input_y - vector['y']) ** 2)
            
            if distance < smallest_distance and distance <= 0.1:
                closest_direction = direction
                smallest_distance = distance

        # Update the last known direction if a new direction is found
        if closest_direction:
            self._last_direction = closest_direction

        return closest_direction, "press"
