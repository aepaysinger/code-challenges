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
    for length, width, height in present_measurements:
        length_x_width = int(length) * int(width)
        width_x_height = int(width) * int(height)
        height_x_length = int(height) * int(length)

        smallest_amount = None

        if length_x_width <= width_x_height and length_x_width <= height_x_length:
            smallest_amount = length_x_width
        elif width_x_height <= length_x_width and width_x_height <= height_x_length:
            smallest_amount = width_x_height
        elif height_x_length <= length_x_width and height_x_length <= width_x_height:
            smallest_amount = height_x_length
        total_wrapping_paper += (
            (length_x_width * 2)
            + (width_x_height * 2)
            + (height_x_length * 2)
            + smallest_amount
        )
    return total_wrapping_paper


def ribbon_for_present():
    present_measurements = find_dimensions()
    total_ribbon = 0
    for length, width, height in present_measurements:
        perimeter = (int(length) * 2) + (int(width) * 2)
        length_and_height = (int(length) * 2) + (int(height) * 2)
        width_and_heght = (int(width) * 2) + (int(height) * 2)
        bow = int(length) * int(width) * int(height)
        ribbon = 0
        if perimeter <= length_and_height and perimeter <= width_and_heght:
            ribbon = perimeter
        elif length_and_height <= perimeter and length_and_height <= width_and_heght:
            ribbon = length_and_height
        elif width_and_heght <= perimeter and width_and_heght <= length_and_height:
            ribbon = width_and_heght
        total_ribbon += ribbon + bow

    return total_ribbon


print(present_dimensions())
print(find_dimensions())
print(find_surface_area())
print(ribbon_for_present())
