def get_bingo_info():
    with open("./code_challenges/advent_of_code/bingo_board_and_numbers") as info:
        numbers = info.read().split("\n")

    numbers = numbers[0].split(",")
    numbers_to_call = [int(number) for number in numbers]
    with open("./code_challenges/advent_of_code/bingo_board_and_numbers") as info:
        boards = info.read().split("\n")
    boards = boards[2:]
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
        for board in boards:
            for row_number, rows in enumerate(boards[board]):
                for i, number in enumerate(rows):
                    if number_to_call == number:
                        boards[board][row_number][i] = "X"
                    if boards[board][row_number] == ["X", "X", "X", "X", "X"]:
                        return boards[board], number
                    for _ in range(len(rows)):
                        if (
                            boards[board][0][_] == "X"
                            and boards[board][1][_] == "X"
                            and boards[board][2][_] == "X"
                            and boards[board][3][_] == "X"
                            and boards[board][4][_] == "X"
                        ):
                            return boards[board], number


def find_winner_score():
    wining_board, winning_number = play_bingo()
    score = 0
    for rows in wining_board:
        for character in rows:
            if character == "X":
                continue
            score += character

    return score * winning_number


def find_last_winning_board():
    boards, numbers_to_call = get_bingo_info()
    winning_boards = set()

    for number_to_call in numbers_to_call:
        for board in boards:
            for row_number, rows in enumerate(boards[board]):
                for i, number in enumerate(rows):
                    if number_to_call == number:
                        boards[board][row_number][i] = "X"
                    if boards[board][row_number] == ["X", "X", "X", "X", "X"]:
                        winning_boards.add(board)
                        if len(winning_boards) == len(boards):
                            return boards[board], number
                    for _ in range(len(rows)):
                        if (
                            boards[board][0][_] == "X"
                            and boards[board][1][_] == "X"
                            and boards[board][2][_] == "X"
                            and boards[board][3][_] == "X"
                            and boards[board][4][_] == "X"
                        ):
                            winning_boards.add(board)
                            if len(winning_boards) == len(boards):
                                return boards[board], number


def find_last_winner_score():
    wining_board, winning_number = find_last_winning_board()
    score = 0
    for rows in wining_board:
        for character in rows:
            if character == "X":
                continue
            score += character

    return score * winning_number
