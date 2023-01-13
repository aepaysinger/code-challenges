def get_directions():

    with open("./code_challenges/advent_of_code/santas_directions") as elf_instructions:
        directions = elf_instructions.read()

    return directions


def follow_directions():
    directions = get_directions()
    x, y = 0, 0
    houses_visited = {(0, 0)}

    for direction in directions:
        if direction == "^":
            x += 1
            houses_visited.add((x, y))
        elif direction == "v":
            x -= 1
            houses_visited.add((x, y))
        elif direction == "<":
            y += 1
            houses_visited.add((x, y))
        elif direction == ">":
            y -= 1
            houses_visited.add((x, y))

    return len(houses_visited)


def robot_santa():
    directions = get_directions()
    robot_x, robot_y = 0, 0
    santa_x, santa_y = 0, 0
    santa_houses = {(0, 0)}
    robot_houses = {(0, 0)}

    for i in range(len(directions)):
        if i % 2 == 0:
            if directions[i] == "^":
                santa_x += 1
                santa_houses.add((santa_x, santa_y))
            elif directions[i] == "v":
                santa_x -= 1
                santa_houses.add((santa_x, santa_y))
            elif directions[i] == "<":
                santa_y += 1
                santa_houses.add((santa_x, santa_y))
            elif directions[i] == ">":
                santa_y -= 1
                santa_houses.add((santa_x, santa_y))
        else:
            if directions[i] == "^":
                robot_x += 1
                robot_houses.add((robot_x, robot_y))
            elif directions[i] == "v":
                robot_x -= 1
                robot_houses.add((robot_x, robot_y))
            elif directions[i] == "<":
                robot_y += 1
                robot_houses.add((robot_x, robot_y))
            elif directions[i] == ">":
                robot_y -= 1
                robot_houses.add((robot_x, robot_y))

        combined_houses = santa_houses | robot_houses

    return len(combined_houses)


# print(get_directions())
# print(follow_directions())
print(robot_santa())
