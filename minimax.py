class Game:
    def __init__(self):
        self.is_terminal = False
        self.value = None
        self.children = None

    def get_value(self):
        return self.value


def minimax(game_state, depth, alpha, beta, max_move):

    if depth == 0 or game_state.is_terminal:
        return game_state.get_value

    if max_move:
        max_evaluation = float("inf")
        for child in game_state.children:
            evaluation = minimax(child, )
    else:
        min_evaluation = -float("inf")
        for child in game_state.children:
            pass
