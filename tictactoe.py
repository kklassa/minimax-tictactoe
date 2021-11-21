import numpy as np


class TicTacToe:
    def __init__(self, rows: int, columns: int, streak_to_win: int):
        self.rows= rows
        self.columns = columns
        self.board = np.zeros((rows, columns))
        self.streak = streak_to_win

    def square_empty(self, row: int, col: int):
        if self.board[row][col] == 0:
            return True
        return False

    def mark_square(self, row: int, col: int, player: int):
        self.board[row][col] = player

    def clear_square(self, row: int, col: int):
        self.board[row][col] = 0

    def empty_squares(self):
        empty_positions = []
        for row in range(self.rows):
            for col in range(self.columns):
                if self.square_empty(row, col):
                    empty_positions.append([row, col])
        return empty_positions

    def check_win(self, player: int):
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

        # left to right diagonal
        for start_row in range(row_offset):
            for start_col in range(col_offset):
                current_streak = 0
                for offset in range(0, self.streak):
                    if self.board[start_row+offset][start_col+offset] == player:
                        current_streak += 1
                    if current_streak == self.streak:
                        return True

        # right to left diagonal
        for start_row in range(row_offset):
            for rigth_offset in range(col_offset):
                start_col = self.columns - rigth_offset -1
                current_streak = 0
                for offset in range(0, self.streak):
                    if self.board[start_row+offset][start_col-offset] == player:
                        current_streak += 1
                    if current_streak == self.streak:
                        return True

        return False

    def generate_heuristic_table(self):
        heuristic_table = np.zeros((self.rows, self.colums))

    def empty_squares_heuristic(self, player: int):
        return player * (len(self.empty_squares()) + 1)
