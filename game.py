import pygame as pg
import sys
import json
import argparse
from tictactoe import TicTacToe


class Player():
    def __init__(self, max_player):
        if max_player:
            self.value = 1
        else:
            self.value = -1

    def make_move(self):
        pass

class MinimaxPlayer(Player):
    def __init__(self, max_player, depth, pruning=True):
        super().__init__(max_player)
        self.depth = depth
        self.pruning = pruning
        self.best_move = None

    def make_move(self, game_state):
        self.minimax(game_state)
        return self.best_move

    def minimax(game_state):
        pass
    '''
    minimax(board):
        get a hold of empty squares array and current board
        for square in board.empty_squares:
            board.mark_square(square)
            if check_win():
                value =  player * (len(empty_squares) + 1)
            else:
                value = minimax(board)

    '''

def create_screen(rows, columns, square_size, foreground_color, background_color):
    width = square_size * columns
    height = square_size * rows
    line_width = int(square_size * 0.1)

    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Tic Tac Toe')
    screen.fill(background_color)

    for i in range(1, columns):
        pg.draw.line(screen, foreground_color, (square_size*i,0), (square_size*i, height), line_width)

    for i in range(1, rows):
        pg.draw.line(screen, foreground_color, (0, square_size*i), (width, square_size*i), line_width)

    return screen


def draw_figures(screen, board, square_size, circle_color, cross_color):
    circe_radius = int(square_size * 0.4)
    edge_width = int(square_size * 0.1)
    cross_offset_1 = int(square_size * 0.24)
    cross_offset_2 = int(square_size * 0.16)

    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            if board[row][col] == 1:
                points = [
                    (col * square_size + cross_offset_1, row * square_size + cross_offset_2),
                    (col * square_size + cross_offset_2, row * square_size + cross_offset_1),
                    (col * square_size + square_size - cross_offset_1, row * square_size + square_size - cross_offset_2),
                    (col * square_size + square_size - cross_offset_2, row * square_size + square_size - cross_offset_1)
                ]
                pg.draw.polygon(screen, cross_color, points)
                points = [
                    (col * square_size + square_size - cross_offset_1, row * square_size + cross_offset_2),
                    (col * square_size + square_size - cross_offset_2, row * square_size + cross_offset_1),
                    (col * square_size + cross_offset_1, row * square_size + square_size - cross_offset_2),
                    (col * square_size + cross_offset_2, row * square_size + square_size - cross_offset_1)
                ]
                pg.draw.polygon(screen, cross_color, points)
            elif board[row][col] == -1:
                pg.draw.circle(screen, circle_color,
                               (int(col * square_size + square_size * 0.5), int(row * square_size + square_size * 0.5)),
                               circe_radius, edge_width)


def main(arguments):

    parser = argparse.ArgumentParser()
    parser.add_argument('--theme')
    args = parser.parse_args(arguments[1:])

    with open('themes.json') as fh:
        themes = json.load(fh)

    if args.theme:
        foreground_color = themes[args.theme][0]['foreground_color']
        background_color = themes[args.theme][0]['background_color']
        x_color = themes[args.theme][0]['x_color']
        o_color = themes[args.theme][0]['o_color']
    else:
        foreground_color = themes['classic'][0]['foreground_color']
        background_color = themes['classic'][0]['background_color']
        x_color = themes['classic'][0]['x_color']
        o_color = themes['classic'][0]['o_color']

    pg.init()
    rows = 5
    columns = 5
    streak = 4
    square_size = 120
    ttt= TicTacToe(rows, columns, streak)
    screen = create_screen(rows, columns, square_size, foreground_color, background_color)

    player = 1 # 1 is X, -1 is O
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0] # x
                mouse_y = event.pos[1] # Y

                clicked_row = int(mouse_y // square_size)
                clicked_col = int(mouse_x // square_size)

                if ttt.square_empty(clicked_row, clicked_col):
                    ttt.mark_square(clicked_row, clicked_col, player)
                    if ttt.check_win(player):
                        winner = 'X' if player == 1 else 'O'
                        print(f'{winner} won')
                    player = - player
                else:
                    print('square full')


        draw_figures(screen, ttt.board, square_size, o_color, x_color)

        pg.display.update()





if __name__=="__main__":
    main(sys.argv)
