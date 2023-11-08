def elves_directions():
    with open(
        "./code_challenges/advent_of_code/directions_to_easter_bunny_hq"
    ) as directions:
        moves = directions.read().split(", ")
    return moves


def follow_directions():
    directions = elves_directions()
    north_south = 0
    east_west = 0
    facing_direction = "N"
    stops = set()
    for (direction, steps) in directions:
        if facing_direction == "N" and direction == "R":
            east_west += int(steps)
            stops.add((east_west, north_south))
            facing_direction = "E"
        elif facing_direction == "N" and direction == "L":
            east_west -= int(steps)
            stops.add((east_west, north_south))
            facing_direction = "W"
        elif facing_direction == "E" and direction == "R":
            north_south -= int(steps)
            stops.add((east_west, north_south))
            facing_direction = "S"
        elif facing_direction == "E" and direction == "L":
            north_south += int(steps)
            stops.add((east_west, north_south))
            facing_direction = "N"
        elif facing_direction == "S" and direction == "R":
            east_west += int(steps)
            stops.add((east_west, north_south))
            facing_direction = "W"
        elif facing_direction == "S" and direction == "L":
            east_west -= int(steps)
            stops.add((east_west, north_south))
            facing_direction = "E"
        elif facing_direction == "W" and direction == "R":
            north_south += int(steps)
            stops.add((east_west, north_south))
            facing_direction = "N"
        elif facing_direction == "W" and direction == "L":
            north_south -= int(steps)
            stops.add((east_west, north_south))
            facing_direction = "S"

        return north_south, east_west




if __name__ == "__main__":
    # print(elves_directions())
    print(follow_directions())