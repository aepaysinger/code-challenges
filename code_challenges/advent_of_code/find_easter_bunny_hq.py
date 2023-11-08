def elves_directions():
    with open(
        "./code_challenges/advent_of_code/directions_to_easter_bunny_hq"
    ) as directions:
        moves = directions.read().split(", ")
    return moves


def find_easter_bunny_hq():
    moves = elves_directions()
    moves = [",".join(move).split(",") for move in moves]
    north_south = 0
    east_west = 0
    direction_facing = "North"
    # print(moves)
    destinations = {(0,0): 1}
    for direction, steps in moves:
        steps = int(steps)
        # print(destinations, direction, steps, "\n")
        if direction == "R" and direction_facing == "North":
            # WORKS!
            for _ in range(east_west + 1, steps + 2):
                destinations[(east_west, north_south)] = 1
                east_west += 1
                if (east_west, north_south) in destinations:
                    return east_west, north_south   
            direction_facing = "East"
            east_west -= 1
        elif direction == "L" and direction_facing == "North":
            #WORKS!
            for _ in range(east_west - 1, east_west + steps):
                destinations[(east_west, north_south)] = 1
                east_west -= 1
                if (east_west, north_south) in destinations:
                    return east_west, north_south
            direction_facing = "West"
            east_west += 1
        elif direction == "R" and direction_facing == "South":
            #WORKS
            for _ in range(east_west - 1, east_west + steps):
                destinations[(east_west, north_south)] = 1
                east_west -= 1
                if (east_west, north_south) in destinations:
                    return east_west, north_south
            direction_facing = "West"
            east_west += 1
        elif direction == "L" and direction_facing == "South":
            #WORKS
            for _ in range(east_west + 1, east_west + steps + 2):
                destinations[(east_west, north_south)] = 1
                east_west += 1
                if (east_west, north_south) in destinations:
                    return east_west, north_south
            direction_facing = "East"
            east_west -= 1
        elif direction == "R" and direction_facing == "East":
            #WORKS
            for _ in range(north_south + 1, steps + 2):
                destinations[(east_west, north_south)] = 1
                north_south -= 1
                if (east_west, north_south) in destinations:
                    return east_west, north_south
            direction_facing = "South"
            north_south += 1
        elif direction == "L" and direction_facing == "East":
            #WORKS
            for _ in range(north_south + 1, steps + 2):
                destinations[(east_west, north_south)] = 1
                north_south += 1
                if (east_west, north_south) in destinations:
                    return east_west, north_south
            direction_facing = "North"
            north_south -= 1
        elif direction == "R" and direction_facing == "West":
            #WORKS
            for _ in range(north_south + 1, steps + 2):
                destinations[(east_west, north_south)] = 1
                north_south += 1
                if (east_west, north_south) in destinations:
                    return east_west, north_south
            direction_facing = "North"
            north_south -= 1
        elif direction == "L" and direction_facing == "West":
            #WORKS
            for _ in range(north_south + 1, steps + 2):
                destinations[(east_west, north_south)] = 1
                north_south -= 1
                if (east_west, north_south) in destinations:
                    return east_west, north_south
            direction_facing = "South"
            north_south += 1
    return destinations
def find_distance():
    east_west, north_south = find_easter_bunny_hq()
    if east_west < 0:
        east_west *= -1
    elif north_south < 0:
        north_south *= -1
    
    return east_west + north_south








# print(elves_directions())
print(find_easter_bunny_hq())
print(find_distance())
# print(first_location_visited_twice())
#not 23
# not 5
#not 21
#not 6