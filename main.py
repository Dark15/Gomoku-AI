import pygame as pg
import constants as c
from sys import exit
import setup


class Main(object):
    def __init__(self):
        self.screen = setup.SCREEN
        self.modes_dict = None
        self.now_mode = None

    def setup_modes(self, modes_dict, mode_name):
        self.modes_dict = modes_dict
        self.now_mode = self.modes_dict[mode_name]
        self.now_mode.startup()

    def update(self):
        if self.now_mode.switch and self.now_mode.switch == c.MENU_MODE:
            self.switch_mode(c.MENU_MODE)
        elif self.now_mode.switch == c.AI_MODE:
            self.switch_mode(c.AI_MODE)
        elif self.now_mode.switch == c.PVP_MODE:
            self.switch_mode(c.PVP_MODE)
        self.now_mode.update(self.screen)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            self.now_mode.get_event(event)

    def switch_mode(self, mode_name):
        self.now_mode = self.modes_dict[mode_name]
        self.now_mode.startup()

    def main(self):
        while True:
            self.event_loop()
            self.update()
            pg.display.update()


class _Mode(object):
    def __init__(self):
        self.switch = False
        self.pos = None

    def update(self, surface):
        pass

    def startup(self):
        pass

    def get_event(self, event):
        pass
