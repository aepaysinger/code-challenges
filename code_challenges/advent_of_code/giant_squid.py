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
    boards_with_number_called = {}
    for number_to_call in numbers_to_call:
        for board in boards:
            for numbers in boards[board]:
                for number in numbers:
                    if number == number_to_call:
                        
                        
            

    return boards

# print(get_bingo_info())
print(play_bingo())