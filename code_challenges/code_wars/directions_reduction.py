def directions_reduction_a(directions):
    new_directions = []

    for direction in directions:
        if new_directions == []:
            new_directions.append(direction)
        elif direction == "NORTH" and new_directions[-1] == "SOUTH":
            new_directions.pop(-1)
        elif direction == "EAST" and new_directions[-1] == "WEST":
            new_directions.pop(-1)
        elif direction == "SOUTH" and new_directions[-1] == "NORTH":
            new_directions.pop(-1)
        elif direction == "WEST" and new_directions[-1] == "EAST":
            new_directions.pop(-1)
        else:
            new_directions.append(direction)

    return new_directions


def directions_reduction_b(directions):
    new_directions = []
    opposite_directions = {
        "NORTH": "SOUTH",
        "EAST": "WEST",
        "SOUTH": "NORTH",
        "WEST": "EAST",
    }
    for direction in directions:
        if new_directions == []:
            new_directions.append(direction)
        elif new_directions[-1] == opposite_directions[direction]:
            new_directions.pop(-1)
        else:
            new_directions.append(direction)
    return new_directions


if __name__ == "__main__":
    directions = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    print(directions_reduction_a(directions))
    print(directions_reduction_b(directions))
