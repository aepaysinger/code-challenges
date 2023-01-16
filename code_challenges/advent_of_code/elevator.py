def elevator_controls_input():
    with open("./code_challenges/advent_of_code/elevator_input") as buttons:
        directions = buttons.read()
    return directions


def find_floor():
    directions = elevator_controls_input()
    final_floor = 0

    for direction in directions:
        if direction == "(":
            final_floor += 1
        elif direction == ")":
            final_floor -= 1

    return final_floor


def enter_basement():
    directions = elevator_controls_input()
    final_floor = 0

    for i in range(len(directions)):
        button = i
        if final_floor < 0:
            break
        if directions[i] == "(":
            final_floor += 1
        elif directions[i] == ")":
            final_floor -= 1

    return button


print(find_floor())
print(enter_basement())
