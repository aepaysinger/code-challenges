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
        length = int(present[0]) * int(present[1])
        width = int(present[1]) * int(present[2])
        height = int(present[2]) * int(present[0])

        smallest_amount = None

        if length <= width and length <= height:
            smallest_amount = length
        elif width <= length and width <= height:
            smallest_amount = width
        elif c <= length and height <= width:
            smallest_amount = height
        total_wrapping_paper += (length * 2) + (width * 2) + (height * 2) + smallest_amount
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
