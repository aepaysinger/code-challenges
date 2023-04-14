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
    # stops = set((0, 0))
    east_west_ranges = []
    north_south_ranges = []
    start_range = 0
    end_range = 0
 
    moves = [move.strip() for move in moves]
    for move in moves:
        left_or_right = move[0]
        steps = int(move[1:])   
        if direction == "N" and left_or_right == "R":
            for east_west_range in east_west_ranges:
                if east_west_range[0] < east_west_range[1]:
                    start_range = east_west_range[0]
                    end_range = east_west_range[1]
                else:
                    start_range = east_west_range[1]
                    end_range = east_west_range[0]
                if steps in range(start_range, end_range):
                    # if north_south < 0:
                    #     north_south *= -1
                    # if east_west < 0:
                    #     east_west *= -1
                    print(f"already been here N/R: {north_south+east_west, steps}")
                    break 
            east_west_ranges.append((east_west, steps))
            direction = "E"
            east_west += steps
            # stops.add((north_south, i))
        elif direction == "N" and left_or_right == "L":
            for east_west_range in east_west_ranges:
                if east_west_range[0] < east_west_range[1]:
                    start_range = east_west_range[0]
                    end_range = east_west_range[1]
                else:
                    start_range = east_west_range[1]
                    end_range = east_west_range[0]
                if steps in range(start_range, end_range):
                    print(f"already been here N/L: {north_south+east_west, steps}")
                    break 
            north_south_ranges.append((north_south, steps))    
            direction = "W"
            east_west -= steps
            # stops.add((north_south, i))
        elif direction == "E" and left_or_right == "R":
            for north_south_range in north_south_ranges:
                if north_south_range[0] < north_south_range[1]:
                    start_range = north_south_range[0]
                    end_range = north_south_range[1]
                else:
                    start_range = north_south_range[1]
                    end_range = north_south_range[0]
                if steps in range(start_range, end_range):
                    print(f"already been here E/R: {north_south+east_west, steps}")
                    break
            north_south_ranges.append((north_south, steps))
            direction = "S"
            north_south -= steps
            # stops.add((i, east_west))
        elif direction == "E" and left_or_right == "L":
            for north_south_range in north_south_ranges:
                if north_south_range[0] < north_south_range[1]:
                    start_range = north_south_range[0]
                    end_range = north_south_range[1]
                else:
                    start_range = north_south_range[1]
                    end_range = north_south_range[0]
                if steps in range(start_range, end_range):
                    print(f"already been here E/L: {north_south+east_west, steps}")
                    break
            north_south_ranges.append((east_west, steps))
            direction = "N"
            north_south += steps
            # stops.add((i, east_west))
        elif direction == "S" and left_or_right == "R":
            for east_west_range in east_west_ranges:
                if east_west_range[0] < east_west_range[1]:
                    start_range = east_west_range[0]
                    end_range = east_west_range[1]
                else:
                    start_range = east_west_range[1]
                    end_range = east_west_range[0]
                if steps in range(start_range, end_range):
                    # if north_south < 0:
                    #     north_south *= -1
                    # if east_west < 0:
                    #     east_west *= -1
                    print(f"already been here S/R: {north_south+east_west, steps}")
                    break 
            east_west_ranges.append((east_west, steps))
            direction = "W"
            east_west -= steps
            # stops.add((north_south, i))
        elif direction == "S" and left_or_right == "L":
            for east_west_range in east_west_ranges:
                if east_west_range[0] < east_west_range[1]:
                    start_range = east_west_range[0]
                    end_range = east_west_range[1]
                else:
                    start_range = east_west_range[1]
                    end_range = east_west_range[0]
                if steps in range(start_range, end_range):
                    print(f"already been here S/L: {north_south+east_west, steps}")
                    break 
            east_west_ranges.append((east_west, steps))
            direction = "E"
            east_west += steps
            # stops.add((north_south, i))
        elif direction == "W" and left_or_right == "R":
            for north_south_range in north_south_ranges:
                if north_south_range[0] < north_south_range[1]:
                    start_range = north_south_range[0]
                    end_range = north_south_range[1]
                else:
                    start_range = north_south_range[1]
                    end_range = north_south_range[0]
                if steps in range(start_range, end_range):
                    print(f"already been here W/R: {north_south+east_west, steps}")
                    break
            north_south_ranges.append((north_south, steps))
            direction = "N"
            north_south += steps
            # stops.add((i, east_west))
        elif direction == "W" and left_or_right == "L":
            for north_south_range in north_south_ranges:
                if north_south_range[0] < north_south_range[1]:
                    start_range = north_south_range[0]
                    end_range = north_south_range[1]
                else:
                    start_range = north_south_range[1]
                    end_range = north_south_range[0]
                if steps in range(start_range, end_range):
                    print(f"already been here W/L: {north_south+east_west, steps}")
                    break
            north_south_ranges.append((north_south, steps))
            direction = "S"
            north_south -= steps
            # stops.add((i, east_west))


    if north_south < 0:
        north_south = north_south * -1
    elif east_west < 0:
        east_west = east_west * -1
    return north_south+east_west, north_south_ranges, east_west_ranges









# print(elves_directions())
print(find_easter_bunny_hq())
# print(first_location_visited_twice())
