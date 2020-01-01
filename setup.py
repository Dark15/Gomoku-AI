import constants as c
import pygame as pg
from pygame import freetype

pg.init()
pg.event.set_blocked([pg.MOUSEMOTION, pg.ACTIVEEVENT, pg.KEYDOWN, pg.KEYUP])
pg.display.set_caption(c.TITLE)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

FONTS = {
    c.OPTION_FONT: freetype.Font(c.OPTION_FONT_DIR),
    c.CAPTION_FONT: freetype.Font(c.CAPTION_FONT)
}
