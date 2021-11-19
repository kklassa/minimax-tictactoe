from tictactoe import TicTacToe


def test_check_win_horizontal_333():
    ttt = TicTacToe(3, 3, 3)
    for col in range(0, 3):
        ttt.mark_square(2, col, -1)
    assert ttt.check_win(-1) == True


def test_check_win_horizontal_554():
    ttt = TicTacToe(5, 5, 4)
    for col in range(1, 5):
        ttt.mark_square(2, col, 1)
    assert ttt.check_win(1) == True


def test_check_win_vertical_333():
    ttt = TicTacToe(3, 3, 3)
    for row in range(0, 3):
        ttt.mark_square(row, 1, -1)
    assert ttt.check_win(-1) == True


def test_check_win_vertical_554():
    ttt = TicTacToe(5, 5, 4)
    for row in range(0, 4):
        ttt.mark_square(row, 3, 1)
    assert ttt.check_win(1) == True


def test_check_win_vertical_696():
    ttt = TicTacToe(6, 9, 6)
    for row in range(0, 6):
        ttt.mark_square(row, 7, 1)
    assert ttt.check_win(1) == True

def test_check_win_left_to_right_diagonal_997():
    ttt = TicTacToe(9, 9, 7)
    for offset in range(0, 8):
        ttt.mark_square(offset, offset, -1)
    assert ttt.check_win(-1) == True

def test_check_win_right_to_left_diagonal_585():
    ttt = TicTacToe(5, 8, 5)
    for offset in range(0, 5):
        ttt.mark_square(offset, 5-offset, 1)
    assert ttt.check_win(1) == True
