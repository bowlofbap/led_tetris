from .ControllerHandler import ControllerHandler
from .TetrisGame import TetrisGame
import argparse

#old way to run the game if you wanna run it manually, go through this file and run game.py

def run_game(debug):
    tetrisGame = TetrisGame()
    gameHandler = ControllerHandler(tetrisGame, debug = debug)

    try:
        gameHandler.start()
    except KeyboardInterrupt:
        gameHandler.clear_screen()

# Main program logic follows:
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", type=bool, help="enables step by step, press b to show path, esc to quit",
                        default=False)
    args = parser.parse_args()
    run_game(args.d)

