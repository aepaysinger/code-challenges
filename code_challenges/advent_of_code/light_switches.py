def get_light_switch_instructions():
    with open("./code_challenges/advent_of_code/light_switch_instructions") as list_of_instructions:
        light_switch_instructions = list_of_instructions.read().split("\n")
    return light_switch_instructions