from sys import exit
import setup
import constants as c
from pygame import freetype
import pygame as pg

pg.init()

screen = pg.display.set_mode((480, 480))
pg.display.set_caption("Test")
# imgsurf = pg.image.load(r'images\background.png')
screen.blit(setup.BG_IMG, (0, 0))
screen.blit(setup.CURSOR_IMG, (95, 220))
screen.blit(setup.CURSOR_IMG, (95, 290))
# screen.blit(setup.bg_white_chess, (95, 290))
screen.blit(setup.CURSOR_IMG, (348, 220))
screen.blit(setup.CURSOR_IMG, (348, 290))
# print(screen.get_rect())
caption = setup.FONT
option = setup.FONT
f, _ = caption.render(c.CAPTION, fgcolor=(0, 0, 0), size=100)
c1, _ = option.render(c.AI_MODE, fgcolor=(133, 133, 133), size=40)
c2, _ = option.render(c.PVP_MODE, fgcolor=(0, 0, 0), size=40)
pg.event.set_blocked([pg.MOUSEMOTION, pg.ACTIVEEVENT, pg.KEYDOWN, pg.KEYUP])

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.MOUSEBUTTONUP:
            print(event.pos)
            print(pg.Rect(c.OPTION1_RECT).collidepoint(event.pos))
            print(pg.Rect(c.OPTION2_RECT).collidepoint(event.pos))
            # print(pg.Rect((0, 0, 480, 480)).collidepoint(event.pos))
        # print(pg.event.event_name(event.type))
        # print(pg.event.event_name(event.type))
    screen.blits(blit_sequence=((f, (100, 60)), (c1, (140, 220)), (c2, (140, 290))))
    pg.display.update()
