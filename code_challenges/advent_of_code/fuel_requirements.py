def get_modules():
    with open("./code_challenges/advent_of_code/module_input") as modules_input:
        modules = modules_input.read().split("\n")

    return [int(module) for module in modules]


def amount_of_fuel():
    modules = get_modules()
    total_fuel = 0
    for module in modules:
        total_fuel += int(module / 3) - 2

    return total_fuel


def fuel_for_fuel():
    modules = get_modules()
    total_fuel = 0
    for module in modules:
        total_fuel += int(module / 3) - 2
        fuel_fuel = int(module / 3) - 2
        while int(fuel_fuel / 3) - 2 > 0:
            fuel_fuel = int(fuel_fuel / 3) - 2
            total_fuel += fuel_fuel

    return total_fuel


if __name__ == "__main__":
    print(fuel_for_fuel())
    # print(amount_of_fuel())
