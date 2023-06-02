def get_bingo_info():
    with open("./code_challenges/advent_of_code/bingo_board_and_numbers") as info:
        data = info.read().split("\n")

    numbers = data[0].split(",")
    numbers_to_call = [int(number) for number in numbers]

    boards = data[2:]
    final_boards = {}
    board_number = 1
    for numbers in boards:
        if numbers == "":
            board_number += 1
            continue
        numbers = numbers.split(" ")
        numbers = [int(number) for number in numbers if number.strip()]
        final_boards[board_number] = final_boards.get(board_number, []) + [numbers]

    return final_boards, numbers_to_call


def play_bingo():
    boards, numbers_to_call = get_bingo_info()

    for number_to_call in numbers_to_call:
        for board_number, board in boards.items():
            for row_number, row in enumerate(board):
                for i, number in enumerate(row):
                    if number_to_call == number:
                        row[i] = "X"
                    if board[row_number] == ["X", "X", "X", "X", "X"]:
                        return board, number
                    for column in range(len(row)):
                        if (
                            board[0][column] == "X"
                            and board[1][column] == "X"
                            and board[2][column] == "X"
                            and board[3][column] == "X"
                            and board[4][column] == "X"
                        ):
                            return board, number


def find_winner_score():
    winning_board, winning_number = play_bingo()
    score = 0
    for row in winning_board:
        for character in row:
            if character == "X":
                continue
            score += character

    return score * winning_number


def find_last_winning_board():
    boards, numbers_to_call = get_bingo_info()
    winning_boards = set()

    for number_to_call in numbers_to_call:
        for board_number, board in boards.items():
            for row_number, row in enumerate(board):
                for i, number in enumerate(row):
                    if number_to_call == number:
                        row[i] = "X"
                        if board[row_number] == ["X", "X", "X", "X", "X"]:
                            winning_boards.add(board_number)
                            if len(winning_boards) == len(boards):
                                return board, number
                        if [i] == "X":
                        # for column in range(len(row)):
                        #     if (
                        #         board[0][column] == "X"
                        #         and board[1][column] == "X"
                        #         and board[2][column] == "X"
                        #         and board[3][column] == "X"
                        #         and board[4][column] == "X"
                        #     ):
                            winning_boards.add(board_number)
                            if len(winning_boards) == len(boards):
                                return board, number


def find_last_winner_score():
    wining_board, winning_number = find_last_winning_board()
    score = 0
    for row in wining_board:
        for character in row:
            if character == "X":
                continue
            score += character

    return score * winning_number
