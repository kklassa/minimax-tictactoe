from random import choice
from tictactoe import TicTacToe
from copy import deepcopy


class Player():
    def __init__(self, max_player):
        self.max_player = max_player
        if max_player:
            self.value = 1
        else:
            self.value = -1
        self.type = 'base'

    def make_move(self, game_state: TicTacToe):
        pass


class HumanPlayer(Player):
    def __init__(self, max_player):
        super().__init__(max_player)
        self.type = 'human'


class RandomPlayer(Player):
    def __init__(self, max_player):
        super().__init__(max_player)
        self.type = 'random'

    def make_move(self, game_state: TicTacToe):
        row, column = choice(game_state.empty_squares())
        return row, column


class MinimaxPlayer(Player):
    def __init__(self, max_player, depth, pruning=True):
        super().__init__(max_player)
        self.depth = depth
        self.pruning = pruning
        self.best_move = None
        self.states_explored = 0
        self.states = {}
        self.type = 'minimax'

    def make_move(self, game_state):
        self.states = {}
        self.minimax(game_state, self.depth, self.max_player)
        if self.max_player:
            row, column = max(self.states, key = self.states.get)
        else:
            row, column = min(self.states, key = self.states.get)
        return row, column

    def minimax(self, game_state: TicTacToe, depth, max_player):
        game_state = deepcopy(game_state)
        self.states_explored += 1
        if game_state.check_win(self.value) or depth == 0:
            return game_state.empty_squares_heuristic(self.value)

        if max_player:
            max_evaluation = -float("inf")
            available_moves = game_state.empty_squares()
            for move in available_moves:
                row, col = move
                player = 1 if max_player else -1
                game_state.mark_square(row, col, player)
                evaluation = self.minimax(game_state, depth-1, False)
                max_evaluation = max(max_evaluation, evaluation)
                if depth == self.depth:
                    self.states[tuple(move)] = max_evaluation
            return max_evaluation
        else:
            min_evaluation = float("inf")
            available_moves = game_state.empty_squares()
            for move in available_moves:
                row, col = move
                player = 1 if max_player else -1
                game_state.mark_square(row, col, player)
                evaluation = self.minimax(game_state, depth-1, True)
                min_evaluation = min(min_evaluation, evaluation)
                if depth == self.depth:
                    self.states[tuple(move)] = min_evaluation
            return min_evaluation

def main():
    ttt= TicTacToe(5, 5, 4)
    max_player = RandomPlayer(True)
    min_player = MinimaxPlayer(False, 3, False)
    turn = 0
    while True:
        current_player = max_player if turn%2 == 0 else min_player
        row, col = current_player.make_move(ttt)
        ttt.mark_square(row, col, current_player.value)
        if ttt.check_win(current_player.value):
            figure = 'X' if current_player.value ==1 else 'O'
            print(f'{figure} won in turn nr {turn +1}')
            break
        turn += 1


if __name__ == "__main__":
    main()
