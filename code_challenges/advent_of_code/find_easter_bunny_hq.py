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
    stops = set((0, 0))
    double_stop = None
    
 
    moves = [move.strip() for move in moves]
    for move in moves:
        left_or_right = move[0]
        steps = move[1:]   
        if direction == "N" and left_or_right == "R":
            direction = "E"
            east_west += int(steps)
            for i in range(int(steps)):
                if (north_south, i) in stops:
                    print(f"i have already been here {(north_south, i)}")
                    double_stop = (north_south, i)
                    break
                else:
                    stops.add((north_south, i))
        elif direction == "N" and left_or_right == "L":
            direction = "W"
            east_west -= int(steps)
            for i in range(int(steps)):
                if (north_south, i) in stops:
                    print(f"i have already been here {(north_south, i)}")
                    double_stop = (north_south, i)
                    break
                else:
                    stops.add((north_south, i))
        elif direction == "E" and left_or_right == "R":
            direction = "S"
            north_south -= int(steps)
            for i in range(int(steps)):
                if (i, east_west) in stops:
                    print(f"i have already been here {(i, east_west)}")
                    double_stop = (i, east_west)
                    break
                else:
                    stops.add((i, east_west))
        elif direction == "E" and left_or_right == "L":
            direction = "N"
            north_south += int(steps)
            for i in range(int(steps)):
                if (i, east_west) in stops:
                    print(f"i have already been here {(i, east_west)}")
                    double_stop = (i, east_west)
                    break
                else:
                    stops.add((i, east_west))
        elif direction == "S" and left_or_right == "R":
            direction = "W"
            east_west -= int(steps)
            for i in range(int(steps)):
                if (north_south, i) in stops:
                    print(f"i have already been here {(north_south, i)}")
                    double_stop = (north_south, i)
                    break
                else:
                    stops.add((north_south, i))
        elif direction == "S" and left_or_right == "L":
            direction = "E"
            east_west += int(steps)
            for i in range(int(steps)):
                if (north_south, i) in stops:
                    print(f"i have already been here {(north_south, i)}")
                    double_stop = (north_south, i)
                    break
                else:
                    stops.add((north_south, i))
        elif direction == "W" and left_or_right == "R":
            direction = "N"
            north_south += int(steps)
            for i in range(int(steps)):
                if (i, east_west) in stops:
                    print(f"i have already been here {(i, east_west)}")
                    double_stop = (i, east_west)
                    break
                else:
                    stops.add((i, east_west))
        elif direction == "W" and left_or_right == "L":
            direction = "S"
            north_south -= int(steps)
            for i in range(int(steps)):
                if (i, east_west) in stops:
                    print(f"i have already been here {(i, east_west)}")
                    double_stop = (i, east_west)
                    break
                else:
                    stops.add((i, east_west))

    if north_south < 0:
        north_south = north_south * -1
    elif east_west < 0:
        east_west = east_west * -1
    

    return north_south+east_west


def first_location_visited_twice():
    moves = elves_directions()
    moves = [move.strip() for move in moves]
    stops = set((0, 0))
    double_stop = None
    north_south = 0
    east_west = 0
    direction = "N"

    for move in moves:
        left_or_right = move[0]
        steps = move[1:]
        print(stops)   
        if direction == "N" and left_or_right == "R":
            direction = "E"
            east_west += int(steps)
            for i in range(1, int(steps)+1):
                if (north_south, i) in stops:
                    print(f"i have already been here {(north_south, i)}")
                    double_stop = [north_south, i]
                    if double_stop[0] < 0:
                        double_stop[0] = double_stop[0] * -1
                    elif double_stop[1] < 0:
                        double_stop[1] = double_stop[1] * -1
                    return double_stop[0] + double_stop[1]
                else:
                    stops.add((north_south, i))
        elif direction == "N" and left_or_right == "L":
            direction = "W"
            east_west -= int(steps)
            for i in range(1, int(steps)+1):
                if (north_south, -i) in stops:
                    print(f"i have already been here {(north_south, -i)}")
                    double_stop = [north_south, -i]
                    if double_stop[0] < 0:
                        double_stop[0] = double_stop[0] * -1
                    elif double_stop[1] < 0:
                        double_stop[1] = double_stop[1] * -1
                    return double_stop[0] + double_stop[1]
                else:
                    stops.add((north_south, -i))
        elif direction == "E" and left_or_right == "R":
            direction = "S"
            north_south -= int(steps)
            for i in range(1, int(steps)+1):
                if (-i, east_west) in stops:
                    print(f"i have already been here {(-i, east_west)}")
                    double_stop = [-i, east_west]
                    if double_stop[0] < 0:
                        double_stop[0] = double_stop[0] * -1
                    elif double_stop[1] < 0:
                        double_stop[1] = double_stop[1] * -1
                    return double_stop[0] + double_stop[1]
                else:
                    stops.add((-i, east_west))
        elif direction == "E" and left_or_right == "L":
            direction = "N"
            north_south += int(steps)
            for i in range(1, int(steps)+1):
                if (i, east_west) in stops:
                    print(f"i have already been here {(i, east_west)}")
                    double_stop = [i, east_west]
                    if double_stop[0] < 0:
                        double_stop[0] = double_stop[0] * -1
                    elif double_stop[1] < 0:
                        double_stop[1] = double_stop[1] * -1
                    return double_stop[0] + double_stop[1]
                else:
                    stops.add((i, east_west))
        elif direction == "S" and left_or_right == "R":
            direction = "W"
            east_west -= int(steps)
            for i in range(1, int(steps)+1):
                if (north_south, -i) in stops:
                    print(f"i have already been here {(north_south, -i)}")
                    double_stop = [north_south, -i]
                    if double_stop[0] < 0:
                        double_stop[0] = double_stop[0] * -1
                    elif double_stop[1] < 0:
                        double_stop[1] = double_stop[1] * -1
                    return double_stop[0] + double_stop[1]
                else:
                    stops.add((north_south, -i))
        elif direction == "S" and left_or_right == "L":
            direction = "E"
            east_west += int(steps)
            for i in range(1, int(steps)+1):
                if (north_south, i) in stops:
                    print(f"i have already been here {(north_south, i)}")
                    double_stop = [north_south, i]
                    if double_stop[0] < 0:
                        double_stop[0] = double_stop[0] * -1
                    elif double_stop[1] < 0:
                        double_stop[1] = double_stop[1] * -1
                    return double_stop[0] + double_stop[1]
                else:
                    stops.add((north_south, i))
        elif direction == "W" and left_or_right == "R":
            direction = "N"
            north_south += int(steps)
            for i in range(1, int(steps)+1):
                if (i, east_west) in stops:
                    print(f"i have already been here {(i, east_west)}")
                    double_stop = [i, east_west]
                    if double_stop[0] < 0:
                        double_stop[0] = double_stop[0] * -1
                    elif double_stop[1] < 0:
                        double_stop[1] = double_stop[1] * -1
                    return double_stop[0] + double_stop[1]
                else:
                    stops.add((i, east_west))
        elif direction == "W" and left_or_right == "L":
            direction = "S"
            north_south -= int(steps)
            for i in range(1, int(steps)+1):
                if (-i, east_west) in stops:
                    print(f"i have already been here {(-i, east_west)}")
                    double_stop = [-i, east_west]
                    if double_stop[0] < 0:
                        double_stop[0] = double_stop[0] * -1
                    elif double_stop[1] < 0:
                        double_stop[1] = double_stop[1] * -1
                    return double_stop[0] + double_stop[1]
                else:
                    stops.add((-i, east_west))





# print(elves_directions())
# print(find_easter_bunny_hq())
print(first_location_visited_twice())
