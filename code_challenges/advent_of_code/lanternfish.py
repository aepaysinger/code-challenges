def get_lanternfish():
    with open("code_challenges/advent_of_code/lanternfish_input") as lanternfish_input:
        lanterfish_count = lanternfish_input.read().split(",")
    return [int(fish) for fish in lanterfish_count]


def count_lanternfish_growth_attempA(days):
    current_lanternfish = get_lanternfish()
    updated_lanternfish = []
    for _ in range(days):
        for fish in current_lanternfish:
            if fish == 0:
                updated_lanternfish.append(8)
                updated_lanternfish.append(6)
            else:
                fish -= 1
                updated_lanternfish.append(fish)
        current_lanternfish = updated_lanternfish
        updated_lanternfish = []
    return len(current_lanternfish)


def count_lanternfish_growth(days):
    lanternfish = get_lanternfish()
    current_lanternfish = {}
    updated_lanternfish = {}
    for fish in lanternfish:
        current_lanternfish[fish] = current_lanternfish.get(fish, 0) + 1

    for _ in range(days):
        for fish, amount in current_lanternfish.items():
            if fish == 0:
                updated_lanternfish[8] = updated_lanternfish.get(8, 0) + amount
                updated_lanternfish[6] = updated_lanternfish.get(6, 0) + amount
                updated_lanternfish[fish] = updated_lanternfish.get(fish, 0)
            elif fish == 1:
                updated_lanternfish[0] = updated_lanternfish.get(0, 0) + amount
                updated_lanternfish[1] = updated_lanternfish.get(1, 0)
            else:
                updated_lanternfish[fish - 1] = (
                    updated_lanternfish.get(fish - 1, 0) + amount
                )
                updated_lanternfish[fish] = updated_lanternfish.get(fish, 0)
        current_lanternfish = updated_lanternfish
        updated_lanternfish = {}

    total_fish = 0
    for fish in current_lanternfish:
        total_fish += current_lanternfish[fish]

    return total_fish
