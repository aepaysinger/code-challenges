class Sudoku:
    def __init__(self, board):
        self.board = board

    def check_rows(self):
        for row in self.board:
            row = set(row)
            if len(row) < 9:
                return False
        return True

    def check_columns(self):
        column_check = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
        }
        for row in self.board:
            for i, column in enumerate(row):
                column_check[i].add(column)
        for column in column_check:
            if len(column_check[column]) != 9 or 0 in column_check[column]:
                return False
        return True

    def check_sections(self):
        top = self.board[:3]

        top_left = set()
        top_middle = set()
        top_right = set()
        for row in top:
            for i, number in enumerate(row):
                if i <= 2:
                    top_left.add(number)
                elif i > 2 and i <= 5:
                    top_middle.add(number)
                elif i > 5 and i <= 8:
                    top_right.add(number)
        if len(top_left) < 9 or len(top_middle) < 9 or len(top_right) < 9:
            return False
        return True

    def win_or_lose(self):
        if self.check_rows() and self.check_columns() and self.check_sections():
            return True
        return False


def validate_sudoku(board):
    sudoku_result = Sudoku(board)

    return sudoku_result.win_or_lose()


if __name__ == "__main__":
    board = [
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
    print(validate_sudoku(board))
