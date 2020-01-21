import constants as c
import pygame as pg
from pygame import freetype
import numpy as np

pg.init()
pg.event.set_blocked([pg.MOUSEMOTION, pg.ACTIVEEVENT, pg.KEYDOWN, pg.KEYUP])
pg.display.set_caption(c.TITLE)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()
FONT = freetype.Font(c.FONT_DIR)

WINS = np.zeros((15, 15, 572), dtype=bool)
count = 0
for row in range(15):
    for col in range(11):
        for k in range(5):
            WINS[row, col + k, count] = True
        count += 1
for row in range(11):
    for col in range(15):
        for k in range(5):
            WINS[row + k, col, count] = True
        count += 1
for row in range(11):
    for col in range(11):
        for k in range(5):
            WINS[row + k, col + k, count] = True
        count += 1
for row in range(4, 15):
    for col in range(11):
        for k in range(5):
            WINS[row - k, col + k, count] = True
        count += 1

FONT_DICT = {
        "CAPTION": FONT.render(c.CAPTION, fgcolor=(0, 0, 0), size=100),
        "OPTION1": FONT.render(c.AI_MODE, fgcolor=(0, 0, 0), size=40),
        "OPTION2": FONT.render(c.PVP_MODE, fgcolor=(0, 0, 0), size=40),
        "BLACK_WIN": FONT.render(c.BLACK_WIN, fgcolor=(0, 0, 0), size=30),
        "WHITE_WIN": FONT.render(c.WHITE_WIN, fgcolor=(0, 0, 0), size=30)
    }

BG_IMG = pg.image.load(r'images\background.png')
CURSOR_IMG = pg.image.load(r'images\cursor.png')
BLACK_CHESS = pg.image.load(r'images\black_chess.png')
WHITE_CHESS = pg.image.load(r'images\white_chess.png')
PREVIOUS_WHITE_CHESS = pg.image.load(r'images\previous_white_chess.png')
PREVIOUS_BLACK_CHESS = pg.image.load(r'images\previous_black_chess.png')




