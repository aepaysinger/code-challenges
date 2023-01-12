def present_dimensions():
    with open(
        "./code_challenges/advent_of_code/present_dimensions_input"
    ) as all_presents:
        present_dimensions = all_presents.read().split("\n")

    return present_dimensions


def find_dimensions():
    all_present_dimensions = present_dimensions()
    present_measurements = [present.split("x") for present in all_present_dimensions]

    return present_measurements


def find_surface_area():
    present_measurements = find_dimensions()
    total_wrapping_paper = 0
    for present in present_measurements:
        a = int(present[0]) * int(present[1])
        b = int(present[1]) * int(present[2])
        c = int(present[2]) * int(present[0])

        smallest_amount = None

        if a <= b and a <= c:
            smallest_amount = a
        elif b <= a and b <= c:
            smallest_amount = b
        elif c <= a and c <= b:
            smallest_amount = c
        total_wrapping_paper += (a * 2) + (b * 2) + (c * 2) + smallest_amount
    return total_wrapping_paper


def ribbon_for_present():
    present_measurements = find_dimensions()
    total_ribbon = 0
    for present in present_measurements:
        perimeter = (int(present[0]) * 2) + (int(present[1]) * 2)
        around_sides_a = (int(present[0]) * 2) + (int(present[2]) * 2)
        arounds_sides_b = (int(present[1]) * 2) + (int(present[2]) * 2)
        bow = int(present[0]) * int(present[1]) * int(present[2])
        ribbon = 0
        if perimeter <= around_sides_a and perimeter <= arounds_sides_b:
            ribbon = perimeter
        elif around_sides_a <= perimeter and around_sides_a <= arounds_sides_b:
            ribbon = around_sides_a
        elif arounds_sides_b <= perimeter and arounds_sides_b <= around_sides_a:
            ribbon = arounds_sides_b
        total_ribbon += ribbon + bow

    return total_ribbon


print(present_dimensions())
print(find_dimensions())
print(find_surface_area())
print(ribbon_for_present())
