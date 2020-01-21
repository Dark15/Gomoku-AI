import pygame as pg
import numpy as np
from pygame import freetype
from sys import exit
import constants as c


def is_true_pos(x, y):
    x_up_left = x // 30 * 30
    y_up_left = y // 30 * 30

    x_up_right = x_up_left + 30
    y_up_right = y_up_left

    x_down_left = x_up_left
    y_down_left = y_up_left + 30

    x_down_right = x_down_left + 30
    y_down_right = y_down_left

    if ((x_up_left - x) ** 2 + (y_up_left - y) ** 2) ** 0.5 <= 10:
        return x_up_left - 14, y_up_left - 14
    if ((x_up_right - x) ** 2 + (y_up_right - y) ** 2) ** 0.5 <= 10:
        return x_up_right - 14, y_up_right - 14
    if ((x_down_left - x) ** 2 + (y_down_left - y) ** 2) ** 0.5 <= 10:
        return x_down_left - 14, y_down_left - 14
    if ((x_down_right - x) ** 2 + (y_down_right - y) ** 2) ** 0.5 <= 10:
        return x_down_right - 14, y_down_right - 14
    return False


# region 初始化游戏
pg.init()

screen = pg.display.set_mode((480, 480))

pg.display.set_caption("Test")
imgsurf = pg.image.load(r'F:\Users\Desktop\Gomoku-AI\images\background.png')
screen.blit(imgsurf, (0, 0))
black = pg.Color('black')
white = pg.Color('white')
chess = pg.image.load(r'images\previous_white_chess.png')
FONT = freetype.Font(c.FONT_DIR)
# endregion

# region 画棋盘
for i in range(15):
    pg.draw.aaline(screen, (0, 0, 0), (30 + i * 30, 30), (30 + i * 30, 450), 1)
    pg.draw.aaline(screen, black, (30, 30 + i * 30), (450, 30 + i * 30), 1)
pg.draw.circle(screen, black, (240, 240), 3)
# endregion

# region 计算所有赢的情况
wins = np.zeros((15, 15, 572), dtype=bool)
my_wins = [0 for i in range(572)]
count = 0
for row in range(15):
    for col in range(11):
        for k in range(5):
            wins[row, col + k, count] = True
        count += 1
for row in range(11):
    for col in range(15):
        for k in range(5):
            wins[row + k, col, count] = True
        count += 1
for row in range(11):
    for col in range(11):
        for k in range(5):
            wins[row + k, col + k, count] = True
        count += 1
for row in range(4, 15):
    for col in range(11):
        for k in range(5):
            wins[row - k, col + k, count] = True
        count += 1

victory_font, _ = FONT.render("白方获胜！", fgcolor=(0, 0, 0), size=30)
screen.blit(victory_font, (190, 3))
# endregion
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key in (pg.K_ESCAPE, pg.K_RETURN):
                exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                bx = event.pos[0]
                by = event.pos[1]
                true_pos = is_true_pos(bx, by)
                if true_pos and (true_pos[0] in range(30, 451)) & (
                        true_pos[1] in range(30, 451)):
                    screen.blit(chess, true_pos)
                    true_x = int(true_pos[0] / 30 - 1)
                    true_y = int(true_pos[1] / 30 - 1)
                    for k in range(572):
                        if wins[true_x][true_y][k]:
                            my_wins[k] += 1
                        if my_wins[k] == 5:
                            print('ojbk')
                            exit()
    pg.display.update()
