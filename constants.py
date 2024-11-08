LED_FREQ_HZ          = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA              = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS       = 20     # Set to 0 for darkest and 255 for brightest
LED_GHOST_BRIGHTNESS = 5
LED_INVERT           = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL          = 0       # set to '1' for GPIOs 13, 19, 41, 45 or

PI = True

#CONSTANTS
BLANK = '.'
#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (255,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 255,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 255)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (255, 255,   0)
LIGHTYELLOW = (175, 175,  20)
CYAN        = (  0, 255, 255)
MAGENTA     = (255,   0, 255)
ORANGE      = (255, 100,   0)

#CONTROLLER INFO for 8bitdo zero 2
CONTROLLER_MAPPING = {
    0: "B",
    1: "A", 
    2: "Y",
    3: "X", 
    4: "L",
    5: "R", 
    8: "Select",
    9: "Start", 
}

COLORS      = (BLUE,GREEN,RED,YELLOW,CYAN,MAGENTA,ORANGE)

WIDTH       = 10
HEIGHT      = 20
 
DIRECTIONS = {
    "left" : {
        'x': -1,
        'y': 0
    },
    "right" : {
        'x': 1,
        'y': 0
    },
    "up" : {
        'x': 0,
        'y': 1
    },
    "down" : {
        'x': 0,
        'y': -1
    },
}

#used to parse the data from bluetooth controllers (x for axis, y for value)
BLUETOOTH_DIRECTIONS = {
    "left" : {
        'x': 0,
        'y': -1
    },
    "right" : {
        'x': 0,
        'y': 1
    },
    "up" : {
        'x': 1,
        'y': -1
    },
    "down" : {
        'x': 1,
        'y': 1
    },
}

BORDERCOLOR = BLUE
BGCOLOR = BLACK
TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GRAY
SIZE = 20
#time before piece moves from holding down
HOLD_DELAY = .2
#time between moving as held down
HOLD_INTERVAL = 0.05
MAX_ROTATIONS = 14
MAX_LEVEL = 15
LINES_PER_LEVEL = 10
INITIAL_SPEED = 0.5
BUFFER = 30