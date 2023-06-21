def get_moves():

    with open(
        "./code_challenges/advent_of_code/supply_stacks_moves"
    ) as move:
        moves = move.read().split("\n")

    return moves


def crates():
    crates = {
        "1": ["F", "T", "C", "L", "R", "P", "G", "Q"],
        "2": ["N", "Q", "H", "W", "R", "F", "S", "J"],
        "3": ["F", "B", "H", "W", "P", "M", "Q"],
        "4": ["V", "S", "T", "D", "F"],
        "5": ["Q", "L", "D", "W", "V", "F", "Z"],
        "6": ["Z", "C", "L", "S"],
        "7": ["Z", "B", "M", "V", "D", "F"],
        "8": ["T", "J", "B"],
        "9": ["Q", "N", "B", "G", "L", "S", "P", "H"],
    }
    return crates


def get_top_crates():
    map_of_crates = crates()
    moves = get_moves()
    moves = [move.split(" ") for move in moves]
    for move in moves:
        for _ in range(int(move[1])):
            # print(map_of_crates[move[5]])
            map_of_crates[move[5]].append(map_of_crates[move[3]].pop())

    top_crates = ""
    for section in map_of_crates:
        top_crates += map_of_crates[section][-1]

    return top_crates


def get_top_crates_update():
    map_of_crates = crates()
    moves = get_moves()
    moves = [move.split(" ") for move in moves]
    for move in moves:
        for i in range(int(move[1]), 0, -1):
            map_of_crates[move[5]].append(map_of_crates[move[3]].pop(-i))

    top_crates = ""
    for section in map_of_crates:
        top_crates += map_of_crates[section][-1]

    return top_crates


print(get_moves())
print(get_top_crates())
print(get_top_crates_update())
