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
            # print(self.states)
            row, column = max(self.states, key = self.states.get)
        else:
            # print(self.states)
            row, column = min(self.states, key = self.states.get)
        return row, column

    def minimax(self, game_state: TicTacToe, depth, max_player):
        game_state = deepcopy(game_state)
        self.states_explored += 1
        player = 1 if max_player else -1
        if depth == 0 or game_state.check_win(self.value):
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

    def minimax2(self, game_state: TicTacToe, depth, max_player):
        game_state = deepcopy(game_state)
        player = 1 if max_player else -1
        if game_state.check_win(player):
            return 10 if player == 1 else -10

        if depth == 0:
            return 0

        available_moves = game_state.empty_squares()
        evaluations = {}
        for move in available_moves:
            # game_state = deepcopy(game_state)
            row, col = move
            player = 1 if max_player else -1
            game_state.mark_square(row, col, player)
            next_player = False if max_player else True
            evaluations[game_state] = self.minimax2(game_state, depth-1, next_player)
        if max_player:
            return max(evaluations, key=evaluations.get)
        else:
            return min(evaluations, key=evaluations.get)




