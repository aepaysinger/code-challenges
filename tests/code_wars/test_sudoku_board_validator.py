from code_challenges.code_wars.sudoku_board_validator import Sudoku, validate_sudoku


def test_sudoku_check_rows():
    sudoku_result = Sudoku(
        [
            [1, 3, 2, 5, 7, 9, 4, 6, 4],
            [4, 9, 8, 2, 6, 1, 3, 7, 5],
            [7, 5, 6, 3, 8, 4, 2, 1, 9],
            [6, 4, 3, 1, 5, 8, 7, 9, 2],
            [5, 2, 1, 7, 9, 3, 8, 4, 6],
            [9, 8, 7, 4, 2, 6, 5, 3, 1],
            [2, 1, 4, 9, 3, 5, 6, 8, 7],
            [3, 6, 5, 8, 1, 7, 9, 2, 4],
            [8, 7, 9, 6, 4, 2, 1, 5, 3],
        ]
    )

    assert sudoku_result.check_rows() == False


def test_sudoku_check_column():
    sudoku_result = Sudoku(
        [
            [1, 3, 2, 5, 7, 9, 4, 6, 8],
            [4, 9, 8, 2, 6, 1, 3, 7, 5],
            [7, 5, 6, 3, 8, 4, 2, 1, 9],
            [6, 7, 3, 1, 5, 8, 7, 9, 2],
            [5, 2, 1, 7, 9, 3, 8, 4, 6],
            [9, 8, 7, 4, 2, 6, 5, 3, 1],
            [2, 1, 4, 9, 3, 5, 6, 8, 7],
            [3, 6, 5, 8, 1, 7, 9, 2, 4],
            [8, 7, 9, 6, 4, 2, 1, 5, 3],
        ]
    )

    assert sudoku_result.check_columns() == False


def test_sudoku_check_sections():
    sudoku_result = Sudoku(
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [9, 1, 2, 3, 4, 5, 6, 7, 8],
        ]
    )

    assert sudoku_result.check_columns() == True

    assert sudoku_result.check_rows() == True

    assert sudoku_result.check_sections() == False


def test_sudoku_win_or_lose():
    sudoku_result = Sudoku(
        [
            [1, 3, 2, 5, 7, 9, 4, 6, 8],
            [4, 9, 8, 2, 6, 1, 3, 7, 5],
            [7, 5, 6, 3, 8, 4, 2, 1, 9],
            [6, 4, 3, 1, 5, 8, 7, 9, 2],
            [5, 2, 1, 7, 9, 3, 8, 4, 6],
            [9, 8, 7, 4, 2, 6, 5, 3, 1],
            [2, 1, 4, 9, 3, 5, 6, 8, 7],
            [3, 6, 5, 8, 1, 7, 9, 2, 4],
            [8, 7, 9, 6, 4, 2, 1, 5, 3],
        ]
    )

    assert sudoku_result.win_or_lose() == True


def test_validate_sudoku():
    actual = validate_sudoku(
        [
            [1, 3, 2, 5, 7, 9, 4, 6, 8],
            [4, 9, 8, 2, 6, 1, 3, 7, 5],
            [7, 5, 6, 3, 8, 4, 0, 1, 9],
            [6, 4, 3, 1, 5, 8, 7, 9, 2],
            [5, 2, 1, 7, 9, 3, 8, 4, 6],
            [0, 8, 7, 4, 2, 6, 5, 3, 1],
            [2, 1, 4, 9, 3, 5, 6, 8, 7],
            [3, 6, 5, 8, 1, 7, 9, 2, 4],
            [8, 7, 9, 6, 0, 2, 1, 5, 3],
        ]
    )
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"
