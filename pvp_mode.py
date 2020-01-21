import main
import constants as c
import setup
import pygame as pg
import time


class PvpMode(main._Mode):
    def __init__(self):
        super().__init__()
        self.now_play = c.BLACK_CHESS
        self.wins = setup.WINS
        self.black_wins = [0 for i in range(572)]
        self.white_wins = [0 for i in range(572)]
        self.white_chess = []
        self.black_chess = []

    def startup(self):
        self.draw_checkerboard()

    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            true_pos = self.is_true_pos(event.pos[0], event.pos[1])
            if all([true_pos,
                    true_pos not in self.white_chess,
                    true_pos not in self.black_chess,
                    true_pos[0] in range(30, 451),
                    true_pos[1] in range(30, 451)]):
                self.draw_checkerboard()
                self.draw_chess(true_pos)
                if self.is_victory(true_pos):
                    self.victory()

    def draw_chess(self, pervious):
        for pos in self.white_chess:
            self.screen.blit(setup.WHITE_CHESS, pos)
        for pos in self.black_chess:
            self.screen.blit(setup.BLACK_CHESS, pos)
        if self.now_play == c.BLACK_CHESS:
            self.screen.blit(setup.PREVIOUS_BLACK_CHESS, pervious)
            self.black_chess.append(pervious)
        else:
            self.screen.blit(setup.PREVIOUS_WHITE_CHESS, pervious)
            self.white_chess.append(pervious)

    def draw_checkerboard(self):
        self.screen.blit(setup.BG_IMG, (0, 0))
        for i in range(15):
            pg.draw.aaline(self.screen, (0, 0, 0), (30 + i * 30, 30), (30 + i * 30, 450), 1)
            pg.draw.aaline(self.screen, (0, 0, 0), (30, 30 + i * 30), (450, 30 + i * 30), 1)
        pg.draw.circle(self.screen, (0, 0, 0), (240, 240), 3)

    def victory(self):
        if self.now_play == c.BLACK_CHESS:
            self.screen.blit(self.font["WHITE_WIN"][0], (185, 3))
        else:
            self.screen.blit(self.font["BLACK_WIN"][0], (190, 3))
        time.sleep(5)
        self.switch = c.MENU_MODE

    def is_victory(self, pos: tuple):
        x = int(pos[0] / 30 - 1)
        y = int(pos[1] / 30 - 1)
        for i in range(572):
            if self.wins[x][y][i] and self.now_play == c.BLACK_CHESS:
                self.black_wins[i] += 1
                self.now_play = c.WHITE_CHESS
                if self.black_wins[i] == 5:
                    return True
            if self.wins[x][y][i] and self.now_play == c.WHITE_CHESS:
                self.white_wins[i] += 1
                self.now_play = c.BLACK_CHESS
                if self.white_wins[i] == 5:
                    return True
        return False

    @staticmethod
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




