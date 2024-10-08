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
FRAME_RATE = 10
REFRESH_RATE = 30
REFRESH_PER_FRAME = REFRESH_RATE // FRAME_RATE

# color
BG_COLOR = color_rgb(30, 30, 30)
FG_COLOR = color_rgb(220, 220, 220)

# snake
INITIAL_SIZE = 10
HEAD_COLOR = color_rgb(200, 200, 200)
BODY_COLOR = color_rgb(25, 115, 200)
SNAKE_PADDING = 0

assert SNAKE_PADDING * 2 < SCALE, \
	f'SNAKE_PADDING too large ({SNAKE_PADDING} >= {SCALE // 2})'

# apple
APPLE_VALUE = 3
APPLE_COLOR = color_rgb(205, 55, 55)
BIG_MULT = 10
BIG_CHANCE = 0.2
BIG_SCALE = 3
BIG_PAD = ((BIG_SCALE - 1) / 2) * SCALE

assert BIG_SCALE > 0 and BIG_SCALE % 2 != 0, \
	f'BIG_SCALE must be an odd number greater than 0'