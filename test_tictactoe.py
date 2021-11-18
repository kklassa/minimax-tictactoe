from tictactoe import TicTacToe


def test_check_win_horizontal():
    ttt = TicTacToe(5, 5, 4)
    for col in range(1, 5):
        ttt.mark_square(2, col, 1)
    assert ttt.check_win(1) == True
