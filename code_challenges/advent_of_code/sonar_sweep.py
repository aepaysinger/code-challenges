def get_sonar_map():
    with open("./code_challenges/advent_of_code/sonar_input") as levels:
        sonar_map = levels.read().split("\n")
    return [int(level) for level in sonar_map]


def find_depth_increase():
    sonar_map = get_sonar_map()
    depth_increase = 0
    for i in range(1, len(sonar_map)):
        if sonar_map[i] > sonar_map[i - 1]:
            depth_increase += 1
    return depth_increase


def find_depth_increase_window():
    sonar_map = get_sonar_map()
    depth_increase = 0
    j = 4
    for i in range(1, len(sonar_map)):
        if sum(sonar_map[i:j]) > sum(sonar_map[i - 1 : j - 1]):
            depth_increase += 1
        j += 1
    return depth_increase
