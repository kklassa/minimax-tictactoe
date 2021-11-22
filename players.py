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
        self.states_explored = 0
        self.states = {}
        self.type = 'minimax'

    def make_move(self, game_state):
        self.states = {}
        if self.pruning:
            self.minimax_alpha_beta(game_state, self.depth, -float("inf"), float("inf"), self.max_player)
        else:
            self.minimax(game_state, self.depth, self.max_player)
        if self.max_player:
            row, column = max(self.states, key = self.states.get)
        else:
            row, column = min(self.states, key = self.states.get)
        return row, column

    def minimax(self, game_state: TicTacToe, depth, max_player):
        game_state = deepcopy(game_state)
        self.states_explored += 1
        player = 1 if max_player else -1
        if game_state.check_win(player):
            return 100 if player == 1 else -100

        if depth == 0:
            return game_state.table_heuristic()


        if max_player:
            max_evaluation = -float("inf")
            available_moves = game_state.empty_squares()
            for move in available_moves:
                new_game_state = deepcopy(game_state)
                row, col = move
                new_game_state.mark_square(row, col, player)
                evaluation = self.minimax(new_game_state, depth-1, False)
                max_evaluation = max(max_evaluation, evaluation)
                if depth == self.depth:
                    self.states[tuple(move)] = evaluation
            return max_evaluation
        else:
            min_evaluation = float("inf")
            available_moves = game_state.empty_squares()
            for move in available_moves:
                new_game_state = deepcopy(game_state)
                row, col = move
                new_game_state.mark_square(row, col, player)
                evaluation = self.minimax(new_game_state, depth-1, True)
                min_evaluation = min(min_evaluation, evaluation)
                if depth == self.depth:
                    self.states[tuple(move)] = evaluation
            return min_evaluation


    def minimax_alpha_beta(self, game_state: TicTacToe, depth, alpha, beta, max_player):
        game_state = deepcopy(game_state)
        self.states_explored += 1
        player = 1 if max_player else -1
        if game_state.check_win(player):
            return 100 if player == 1 else -100

        if depth == 0:
            return game_state.table_heuristic()


        if max_player:
            max_evaluation = -float("inf")
            available_moves = game_state.empty_squares()
            for move in available_moves:
                new_game_state = deepcopy(game_state)
                row, col = move
                new_game_state.mark_square(row, col, player)
                evaluation = self.minimax_alpha_beta(new_game_state, depth-1, alpha, beta, False)
                max_evaluation = max(max_evaluation, evaluation)
                if depth == self.depth:
                    self.states[tuple(move)] = evaluation
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_evaluation
        else:
            min_evaluation = float("inf")
            available_moves = game_state.empty_squares()
            for move in available_moves:
                new_game_state = deepcopy(game_state)
                row, col = move
                new_game_state.mark_square(row, col, player)
                evaluation = self.minimax_alpha_beta(new_game_state, depth-1, alpha, beta, True)
                min_evaluation = min(min_evaluation, evaluation)
                if depth == self.depth:
                    self.states[tuple(move)] = evaluation
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return min_evaluation