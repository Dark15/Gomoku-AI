import constants as c
import pygame as pg
from pygame import freetype

pg.init()
pg.event.set_blocked([pg.MOUSEMOTION, pg.ACTIVEEVENT, pg.KEYDOWN, pg.KEYUP])
pg.display.set_caption(c.TITLE)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

FONT = freetype.Font(c.FONT_DIR)

FONT_DICT = {
        "CAPTION": FONT.render(c.CAPTION, fgcolor=(0, 0, 0), size=100),
        "OPTION1": FONT.render(c.AI_MODE, fgcolor=(0, 0, 0), size=40),
        "OPTION2": FONT.render(c.PVP_MODE, fgcolor=(0, 0, 0), size=40)
    }
bg_img = pg.image.load(r'images\background.png')
cursor_img = pg.image.load(r'images\white1.png')



