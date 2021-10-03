import ctypes
from math import floor

from graphics import color_rgb

# screen
SCREEN_WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
SCREEN_HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)

# window
MAX_WIDTH = 1000
MAX_HEIGHT = 600
SCALE = 20
WIDTH = floor(MAX_WIDTH / SCALE) * SCALE
HEIGHT = floor(MAX_HEIGHT / SCALE) * SCALE
WIN_X = (SCREEN_WIDTH - WIDTH) // 2
WIN_Y = (SCREEN_HEIGHT - HEIGHT) // 2 - 50

# timing
FRAMERATE = 10

# color
BG_COLOR = color_rgb(30, 30, 30)
FG_COLOR = color_rgb(220, 220, 220)

# snake
INITIAL_SIZE = 10
HEAD_COLOR = color_rgb(200, 200, 200)
BODY_COLOR = color_rgb(25, 115, 200)

# apple
APPLE_VALUE = 3
BIG_MULT = 10
BIG_CHANCE = 0.1
APPLE_COLOR = color_rgb(205, 55, 55)
