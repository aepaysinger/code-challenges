def get_rps_moves():
    with open(
        "/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/rps_input"
    ) as elf_guide:
        moves = elf_guide.read().split("\n")

    return moves


def rps():

    moves = get_rps_moves()
    """
     elf_rock = "A"
     elf_paper = "B"
     elf_scissors = "C"
     rock = "X" lose
     paper = "Y" draw
     scissors = "Z" win
     "X" = lose
     "Y" = draw
     "Z" = win
    """
    points = 0
    for move in moves:
        move = move.split(" ")
        if move[0] == "A":
            if move[1] == "X":
                points += 3
            elif move[1] == "Y":
                points += 4
            elif move[1] == "Z":
                points += 8
        elif move[0] == "B":
            if move[1] == "X":
                points += 1
            elif move[1] == "Y":
                points += 5
            elif move[1] == "Z":
                points += 9
        elif move[0] == "C":
            if move[1] == "X":
                points += 2
            elif move[1] == "Y":
                points += 6
            elif move[1] == "Z":
                points += 7

    return points


print(rps())
