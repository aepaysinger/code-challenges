def get_directions():
    with open("./code_challenges/advent_of_code/directions_input") as input:
        directions = input.read().split("\n")
    return [direction.split(" ") for direction in directions]


def find_depth():
    directions = get_directions()
    horizontal = 0
    depth = 0
    for direction in directions:
        if direction[0] == "forward":
            horizontal += int(direction[1])
        elif direction[0] == "down":
            depth += int(direction[1])
        elif direction[0] == "up":
            depth -= int(direction[1])

    return horizontal * depth


def find_depth_with_aim():
    directions = get_directions()
    horizontal = 0
    depth = 0
    aim = 0

    for direction, amount in directions:
        if direction == "down":
            aim += int(amount)
        elif direction == "up":
            aim -= int(amount)
        elif direction == "forward":
            horizontal += int(amount)
            depth += aim * int(amount)
    return horizontal * depth


print(get_directions())
# print(find_depth())
# print(find_depth_with_aim())
