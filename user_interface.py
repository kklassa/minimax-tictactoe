import pygame as pg
import json


class UI:
    def __init__(self, rows, columns, square_size):
        self.rows = rows
        self.columns = columns
        self.square_size = square_size
        self.screen = None
        self.color_theme = None


    def set_color_theme(self, theme_name):
        with open('themes.json') as fh:
            themes = json.load(fh)

        if theme_name:
            self.color_theme =themes[theme_name][0]
        else:
            self.color_theme =themes['classic'][0]


    def draw_lines(self, width, height):
        line_width = int(self.square_size * 0.1)
        for i in range(1, self.columns):
            pg.draw.line(self.screen, self.color_theme['foreground_color'], (self.square_size*i,0), (self.square_size*i, height), line_width)

        for i in range(1, self.rows):
            pg.draw.line(self.screen, self.color_theme['foreground_color'], (0, self.square_size*i), (width, self.square_size*i), line_width)


    def create_screen(self):
        width = self.square_size * self.columns
        height = self.square_size * self.rows
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption('Tic Tac Toe')
        self.screen.fill(self.color_theme['background_color'])
        self.draw_lines(width, height)


    def reset(self):
        width = self.square_size * self.columns
        height = self.square_size * self.rows
        self.screen.fill(self.color_theme['background_color'])
        self.draw_lines(width, height)


    def draw_figures(self, board):
        circe_radius = int(self.square_size * 0.4)
        edge_width = int(self.square_size * 0.1)
        cross_offset_1 = int(self.square_size * 0.24)
        cross_offset_2 = int(self.square_size * 0.16)

        for row in range(board.shape[0]):
            for col in range(board.shape[1]):
                if board[row][col] == 1:
                    points = [
                        (col * self.square_size + cross_offset_1, row * self.square_size + cross_offset_2),
                        (col * self.square_size + cross_offset_2, row * self.square_size + cross_offset_1),
                        (col * self.square_size + self.square_size - cross_offset_1, row * self.square_size + self.square_size - cross_offset_2),
                        (col * self.square_size + self.square_size - cross_offset_2, row * self.square_size + self.square_size - cross_offset_1)
                    ]
                    pg.draw.polygon(self.screen, self.color_theme['x_color'], points)
                    points = [
                        (col * self.square_size + self.square_size - cross_offset_1, row * self.square_size + cross_offset_2),
                        (col * self.square_size + self.square_size - cross_offset_2, row * self.square_size + cross_offset_1),
                        (col * self.square_size + cross_offset_1, row * self.square_size + self.square_size - cross_offset_2),
                        (col * self.square_size + cross_offset_2, row * self.square_size + self.square_size - cross_offset_1)
                    ]
                    pg.draw.polygon(self.screen, self.color_theme['x_color'], points)
                elif board[row][col] == -1:
                    pg.draw.circle(self.screen, self.color_theme['o_color'],
                                (int(col * self.square_size + self.square_size * 0.5), int(row * self.square_size + self.square_size * 0.5)),
                                circe_radius, edge_width)
