import main
import constants as c
import setup
import pygame as pg
from pygame import freetype


class Menu(main._Mode):
    def __init__(self):
        super().__init__()
        self.background = None
        self.caption_font = None
        self.option_font = None
        # self.option = None
        self.font = setup.FONT_DICT

    def startup(self):
        self.setup_background()

    def setup_background(self):
        self.background = setup.bg_img
        self.caption_font = setup.FONT
        self.option_font = setup.FONT

    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.switch = self.check_pos()

    def check_pos(self):
        if pg.Rect(c.OPTION1_RECT).collidepoint(pg.mouse.get_pos()):
            self.font["OPTION1"] = setup.FONT.render(c.AI_MODE, fgcolor=(133, 133, 133), size=40)
            return c.AI_MODE
        if pg.Rect(c.OPTION2_RECT).collidepoint(pg.mouse.get_pos()):
            self.font["OPTION2"] = setup.FONT.render(c.PVP_MODE, fgcolor=(133, 133, 133), size=40)
            return c.PVP_MODE
        return False

    def update(self, surface):
        surface.blit(setup.bg_img, (0, 0))
        if self.check_pos() == c.AI_MODE:
            surface.blit(setup.cursor_img, (95, 220))
            surface.blit(setup.cursor_img, (348, 220))
        elif self.check_pos() == c.PVP_MODE:
            surface.blit(setup.cursor_img, (95, 290))
            surface.blit(setup.cursor_img, (348, 290))
        else:
            self.font["OPTION1"] = setup.FONT.render(c.AI_MODE, fgcolor=(0, 0, 0), size=40)
            self.font["OPTION2"] = setup.FONT.render(c.PVP_MODE, fgcolor=(0, 0, 0), size=40)
        surface.blits(blit_sequence=((self.font['CAPTION'][0], (100, 60)), 
                                     (self.font['OPTION1'][0], (140, 220)), 
                                     (self.font['OPTION2'][0], (140, 290))))
        # surface.bilts(...)
