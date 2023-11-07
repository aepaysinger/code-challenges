def tetris(moves):
    count = 0
    board = []
    for i in range(30):
        column = []
        for j in range(9):
            column.append("-")
        board.append(column)
    updated_board = board
    positions = {
        "L4": 0,
        "L3": 1,
        "L2": 2,
        "L1": 3,
        "L0": 4,
        "R0": 4,
        "R1": 5,
        "R2": 6,
        "R3": 7,
        "R4": 8,
    }

    for height, side, position in moves:
        move_count = 0

        for i, column in enumerate(board):
            if i == 29 and move_count < int(height):
                return count
            if move_count == int(height):
                break
            if column[positions[side + position]] == "-":
                updated_board[i][positions[side + position]] = "x"
                move_count += 1

        board = updated_board
        board, removed = check_for_full_row(board)
        count += removed

    return count


def check_for_full_row(board):
    removed = 0
    while board[0] == ["x", "x", "x", "x", "x", "x", "x", "x", "x"]:
        board.pop(0)
        board.append(["-", "-", "-", "-", "-", "-", "-", "-", "-"])
        removed += 1
    return board, removed
