def elves_directions():
    with open(
        "./code_challenges/advent_of_code/directions_to_easter_bunny_hq"
    ) as directions:
        moves = directions.read().split(",")
    return moves


def find_easter_bunny_hq():
    moves = elves_directions()
    north_south = 0
    east_west = 0
    direction = "N"
    for move in moves:
        move = move.strip()
        print(direction, north_south, east_west)    
        if direction == "N" and move[0] == "R":
            direction = "E"
            east_west += int(move[1])
        elif direction == "N" and move[0] == "L":
            direction = "W"
            east_west -= int(move[1])
        elif direction == "E" and move[0] == "R":
            direction = "S"
            north_south -= int(move[1])
        elif direction == "E" and move[0] == "L":
            direction = "N"
            north_south += int(move[1])
        elif direction == "S" and move[0] == "R":
            direction = "W"
            east_west -= int(move[1])
        elif direction == "S" and move[0] == "L":
            direction = "E"
            east_west += int(move[1])
        elif direction == "W" and move[0] == "R":
            direction = "N"
            north_south += int(move[1])
        elif direction == "W" and move[0] == "L":
            direction = "S"
            north_south -= int(move[1])

    if north_south < 0:
        north_south = north_south * -1
    elif east_west < 0:
        east_west = east_west * -1
    

    return north_south, east_west



print(elves_directions())
print(find_easter_bunny_hq())