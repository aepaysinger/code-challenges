def get_crab_positions():
    with open("code_challenges/advent_of_code/crab_positions_input") as all_crabs:
        crab_postions = all_crabs.read().split(",")

    return sorted([int(crab_position) for crab_position in crab_postions])


def fuel_spent_to_align_position():
    crab_positions = get_crab_positions()
    middle_point = crab_positions[len(crab_positions) // 2]
    total_fuel = 0
    for crab_position in crab_positions:
        if crab_position > middle_point:
            total_fuel += crab_position - middle_point
        elif crab_position < middle_point:
            total_fuel += middle_point - crab_position

    return total_fuel


def find_fuel_total(crab_positions, align_position):
    total_fuel = 0
    for crab_position in crab_positions:
        if crab_position > align_position:
            location_total = crab_position - align_position
            for i in range(1, location_total + 1):
                total_fuel += i
        elif crab_position < align_position:
            location_total = align_position - crab_position
            for i in range(1, location_total + 1):
                total_fuel += i
    return total_fuel


def fuel_spent_to_align_position_part2():
    crab_positions = get_crab_positions()
    align_position = round(sum(crab_positions) / len(crab_positions))
    align_position_b = sum(crab_positions) // len(crab_positions)
    total_fuel = find_fuel_total(crab_positions, align_position)
    total_fuel_b = find_fuel_total(crab_positions, align_position_b)

    if total_fuel < total_fuel_b:
        return total_fuel
    else:
        return total_fuel_b
