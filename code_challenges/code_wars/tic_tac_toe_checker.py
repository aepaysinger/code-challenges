def find_winner(board):

    ways_to_win = {
        0: [board[0][0], board[0][1], board[0][2]],
        1: [board[0][0], board[1][0], board[2][0]],
        2: [board[0][1], board[1][1], board[2][1]],
        3: [board[0][2], board[1][2], board[2][2]],
        4: [board[0][0], board[1][1], board[2][2]],
        5: [board[1][0], board[1][1], board[1][2]],
        6: [board[2][0], board[2][1], board[2][2]],
        7: [board[0][2], board[1][1], board[2][0]],

    }
    for moves in ways_to_win:
        if ways_to_win[moves] == [1, 1, 1]:
            return 1
        elif ways_to_win[moves] == [2, 2, 2]:
            return 2
    for moves in ways_to_win:
        if 0 in ways_to_win[moves]:
            return -1
    return 0


if __name__ == "__main__":
    board = [[2, 1, 2],
             [1, 1, 1],
             [2, 2, 1]]
    print(find_winner(board))


