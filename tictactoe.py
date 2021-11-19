import numpy as np


class TicTacToe:
    def __init__(self, rows, columns, streak_to_win):
        self.rows= rows
        self.columns = columns
        self.board = np.zeros((rows, columns))
        self.streak = streak_to_win

    def square_empty(self, row, col):
        if self.board[row][col] == 0:
            return True
        return False

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def clear_square(self, row, col):
        self.board[row][col] = 0

    def empty_squares(self):
        empty_positions = []
        for row in range(self.rows):
            for col in range(self.columns):
                if self.square_empty(row, col):
                    empty_positions.append([row, col])
        return empty_positions

    def check_win(self, player):
        # 0 for draw, 1 for X win, -1 for O win
        row_offset = self.rows - self.streak + 1
        col_offset = self.columns - self.streak + 1

        # horizontal
        for row in range(self.rows):
            for start_col in range(col_offset):
                current_streak = 0
                for col in range(start_col, start_col+self.streak):
                    if self.board[row][col] == player:
                        current_streak +=1
                    if current_streak == self.streak:
                        return True

        # vertical
        for col in range(self.columns):
            for start_row in range(row_offset):
                current_streak = 0
                for row in range(start_row, start_row+self.streak):
                    if self.board[row][col] == player:
                        current_streak +=1
                    if current_streak == self.streak:
                        return True


        return False

    def generate_heuristic_table(self):
        heuristic_table = np.zeros((self.rows, self.colums))