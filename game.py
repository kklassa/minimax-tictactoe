import pygame as pg
import argparse
import sys
from time import sleep
from tictactoe import TicTacToe
from players import Player, HumanPlayer, RandomPlayer, MinimaxPlayer
from user_interface import UI


def game_loop(game: TicTacToe, max_player: Player, min_player: Player, ui: UI):
    turn = 0
    current_player = None
    game_over = False
    while not game_over:
        current_player = max_player if turn%2 == 0 else min_player
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if current_player.type == 'human':

                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_x = event.pos[0] # x
                    mouse_y = event.pos[1] # Y

                    clicked_row = int(mouse_y // ui.square_size)
                    clicked_col = int(mouse_x // ui.square_size)

                    if game.square_empty(clicked_row, clicked_col):
                        game.mark_square(clicked_row, clicked_col, current_player.value)
                        if game.check_win(current_player.value):
                            winner = 'X' if current_player.value == 1 else 'O'
                            print(f'{winner} won in turn nr {turn+1}')
                            game_over = True
                        turn += 1
                    else:
                        print('square full')

        if len(game.empty_squares()) == 0:
            print('draw')
            game_over = True
        elif  current_player.type != 'human':
            print(game.board)
            print(f'current score evaluation: {game.table_heuristic()}')
            sleep(0.5)
            # print(f' Player {current_player.value} moves')
            row, col = current_player.make_move(game)
            game.mark_square(row, col, current_player.value)
            if game.check_win(current_player.value):
                winner = 'X' if current_player.value == 1 else 'O'
                print(f'{winner} won in turn nr {turn+1}')
                game_over = True
            turn += 1

        ui.draw_figures(game.board)
        pg.display.update()

        if game_over:
            sleep(3)

    return current_player, turn


def main(arguments):

    parser = argparse.ArgumentParser()
    parser.add_argument('--theme')
    args = parser.parse_args(arguments[1:])

    rows = 3
    columns = 3
    streak = 3
    square_size = 120
    ttt= TicTacToe(rows, columns, streak)
    pg.init()
    ui = UI(rows, columns, square_size)
    ui.set_color_theme(args.theme)
    ui.create_screen()

    #max_player = HumanPlayer(True)
    max_player = MinimaxPlayer(True, 9, False)
    min_player = MinimaxPlayer(False, 9, False)

    game_loop(ttt, max_player, min_player, ui)


if __name__=="__main__":
    main(sys.argv)
