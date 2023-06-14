def get_vents_input():
    with open("code_challenges/advent_of_code/vents_input") as vents_input:
        vents_coordinates = vents_input.read().split("\n")

    vents_coordinates = [
        vent_coordinate.split("->") for vent_coordinate in vents_coordinates
    ]
    vents_coordinates = [
        coordinate.strip()
        for vent_coordinate in vents_coordinates
        for coordinate in vent_coordinate
    ]
    vents_coordinates = [
        vent_coordinate.split(",") for vent_coordinate in vents_coordinates
    ]

    return vents_coordinates


def get_coordinate_pairs():
    vents_coordinates = get_vents_input()
    coordinate_pairs = []

    biggest_x = 0
    biggest_y = 0
    j = 1
    i = 0
    for coordinates in vents_coordinates:
        if j > len(vents_coordinates):
            break
        coordinate_pairs.append(
            [
                (int(vents_coordinates[i][0]), int(vents_coordinates[i][1])),
                (int(vents_coordinates[j][0]), int(vents_coordinates[j][1])),
            ]
        )
        i += 2
        j += 2

    for coordinates in coordinate_pairs:
        for x, y in coordinates:
            if x > biggest_x:
                biggest_x = x
            if y > biggest_y:
                biggest_y = y

    return coordinate_pairs, biggest_x, biggest_y


def mark_coordinates_horizontal_vertical():
    coordinate_pairs, biggest_x, biggest_y = get_coordinate_pairs()
    coordinates_map = [[0 for i in range(biggest_x + 1)] for i in range(biggest_y + 1)]
    x = 0
    y = 1

    for (x1, y1), (x2, y2) in coordinate_pairs:
        if y1 == y2:
            if x1 < x2:
                for coordinate in range(x1, x2 + 1):
                    coordinates_map[y1][coordinate] += 1
            else:
                for coordinate in range(x2, x1 + 1):
                    coordinates_map[y1][coordinate] += 1
        elif x1 == x2:
            if y2 < y1:
                for coordinate in range(y2, y1 + 1):
                    coordinates_map[coordinate][x1] += 1
            else:
                for coordinate in range(y1, y2 + 1):
                    coordinates_map[coordinate][x1] += 1

    danger_zone = 0
    for coordinates in coordinates_map:
        for coordinate in coordinates:
            if coordinate >= 2:
                danger_zone += 1
    return danger_zone


def mark_coordinates_horizontal_vertical_diagonal():
    coordinate_pairs, biggest_x, biggest_y = get_coordinate_pairs()
    coordinates_map = [[0 for i in range(biggest_x + 1)] for i in range(biggest_y + 1)]
    x = 0
    y = 1
    for (x1, y1), (x2, y2) in coordinate_pairs:
        if y1 == y2:
            if x1 < x2:
                for coordinate in range(x1, x2 + 1):
                    coordinates_map[y1][coordinate] += 1
            else:
                for coordinate in range(x2, x1 + 1):
                    coordinates_map[y1][coordinate] += 1
        elif x1 == x2:
            if y2 < y1:
                for coordinate in range(y2, y1 + 1):
                    coordinates_map[coordinate][x1] += 1
            else:
                for coordinate in range(y1, y2 + 1):
                    coordinates_map[coordinate][x1] += 1
        elif x2 < x1 and y2 < y1:
            x_coordinate = x2
            for coordinate in range(y2, y1 + 1):
                coordinates_map[coordinate][x_coordinate] += 1
                x_coordinate += 1
        elif x1 < x2 and y1 > y2:
            x_coordinate = x2
            for coordinate in range(y2, y1 + 1):
                coordinates_map[coordinate][x_coordinate] += 1
                x_coordinate -= 1
        elif x1 < x2 and y1 < y2:
            x_coordinate = x1
            for coordinate in range(x1, x2 + 1):
                coordinates_map[coordinate][coordinate] += 1
        elif x2 < x1 and y2 > y1:
            y_coordinate = y2
            for coordinate in range(x2, x1 + 1):
                coordinates_map[coordinate][y_coordinate] += 1
                y_coordinate -= 1

    danger_zone = 0
    for coordinates in coordinates_map:
        for coordinate in coordinates:
            if coordinate >= 2:
                danger_zone += 1

    return danger_zone


# print(get_vents_input())
# print(mark_coordinates_horizontal_vertical())
print(mark_coordinates_horizontal_vertical_diagonal())
# print(get_coordinate_pairs())
# 19424 too lovw
