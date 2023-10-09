def get_key_pad_moves():
    with open("code_challenges/advent_of_code/key_pad_moves") as input:
        key_pay_moves = input.read().split("\n")
    return key_pay_moves


def find_code():
    key_pad_moves = get_key_pad_moves()
    key_pad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    code = ""
    destination_row = 1
    destination_column = 1

    for line in key_pad_moves:
        for move in line:
            if move == "U" and destination_row > 0:
                destination_row -= 1
            elif move == "L" and destination_column > 0:
                destination_column -= 1
            elif move == "R" and destination_column < 2:
                destination_column += 1
            elif move == "D" and destination_row < 2:
                destination_row += 1
        code += key_pad[destination_row][destination_column]
    return code


def find_code_2():
    key_pad_moves = get_key_pad_moves()
    key_pad = [
        ["X", "X", "1", "X", "X"],
        ["X", "2", "3", "4", "X"],
        ["5", "6", "7", "8", "9"],
        ["X", "A", "B", "C", "X"],
        ["X", "X", "D", "X", "X"],
    ]
    code = ""
    destination_row = 2
    destination_column = 0

    for line in key_pad_moves:
        for move in line:
            if move == "U" and destination_row > 0:
                if destination_row == 1 and destination_column == 2:
                    destination_row -= 1
                elif (destination_row == 2 or destination_row == 3) and (
                    destination_column == 1
                    or destination_column == 2
                    or destination_column == 3
                ):
                    destination_row -= 1
                elif destination_row == 4 and destination_column == 2:
                    destination_row -= 1
            elif move == "L" and destination_column > 0:
                if (destination_row == 1 or destination_row == 3) and (
                    destination_column == 2 or destination_column == 3
                ):
                    destination_column -= 1
                elif destination_row == 2:
                    destination_column -= 1
            elif move == "R" and destination_column < 4:
                if (destination_row == 1 or destination_row == 3) and (
                    destination_column == 1 or destination_column == 2
                ):
                    destination_column += 1
                elif destination_row == 2:
                    destination_column += 1
            elif move == "D" and destination_row < 4:
                if (
                    destination_row == 0 or destination_row == 3
                ) and destination_column == 2:
                    destination_row += 1
                elif (destination_row == 1 or destination_row == 2) and (
                    destination_column == 1
                    or destination_column == 2
                    or destination_column == 3
                ):
                    destination_row += 1

        code += key_pad[destination_row][destination_column]

    return code
