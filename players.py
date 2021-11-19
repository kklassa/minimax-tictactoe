
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