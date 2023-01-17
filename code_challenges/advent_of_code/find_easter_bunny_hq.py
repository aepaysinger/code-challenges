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

    moves = [move.strip() for move in moves]
    visited_locations = [(0,0)]
    for move in moves:
        left_or_right = move[0]
        steps = move[1:]   
        if direction == "N" and left_or_right == "R":
            direction = "E"
            east_west += int(steps)
        elif direction == "N" and left_or_right == "L":
            direction = "W"
            east_west -= int(steps)
        elif direction == "E" and left_or_right == "R":
            direction = "S"
            north_south -= int(steps)
        elif direction == "E" and left_or_right == "L":
            direction = "N"
            north_south += int(steps)
        elif direction == "S" and left_or_right == "R":
            direction = "W"
            east_west -= int(steps)
        elif direction == "S" and left_or_right == "L":
            direction = "E"
            east_west += int(steps)
        elif direction == "W" and left_or_right == "R":
            direction = "N"
            north_south += int(steps)
        elif direction == "W" and left_or_right == "L":
            direction = "S"
            north_south -= int(steps)

        visited_locations.append((north_south, east_west))

    if north_south < 0:
        north_south = north_south * -1
    elif east_west < 0:
        east_west = east_west * -1
    

    return north_south+east_west, visited_locations


# def first_location_visited_twice():
#     moves = elves_directions()
#     moves = [move.strip() for move in moves]




# print(elves_directions())
print(find_easter_bunny_hq())