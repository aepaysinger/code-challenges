def get_vents_input():
    with open("code_challenges/advent_of_code/vents_input") as vents_input:
        vents_coordinates = vents_input.read().split("\n")

    return vents_coordinates


def transform_vents_input():
    vents_coordinates = get_vents_input()
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
    vents_coordinates = transform_vents_input()
    coordinate_pairs = []

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


    return coordinate_pairs

def count_coordinate_points():
    coordinate_pairs = get_coordinate_pairs()
    coordinate_points = {}
    count = 0
    for (x1, y1), (x2, y2) in coordinate_pairs:
        if y1 == y2:
            if x1 < x2:
                for coordinate in range(x1, x2 + 1):
                    coordinate_points[(coordinate, y1)] = coordinate_points.get((coordinate, y1), 0) + 1
            else:
                for coordinate in range(x2, x1 + 1):
                    coordinate_points[(coordinate, y1)] = coordinate_points.get((coordinate, y1), 0) + 1
        elif x1 == x2:
            if y1 < y2:
                for coordinate in range(y1, y2 +1):
                    coordinate_points[(x1, coordinate)] = coordinate_points.get((x1, coordinate), 0) + 1
            else: 
                for coordinate in range(y2, y1 + 1):
                    coordinate_points[(x1, coordinate)] = coordinate_points.get((x1, coordinate), 0) + 1
        elif x1 < x2 and y1 < y2:
            x_coordinate = x1
            for coordinate in range(x1, x2 +1):
                coordinate_points[(coordinate, x_coordinate)] = coordinate_points.get((coordinate, x_coordinate), 0) + 1
                x_coordinate += 1
        elif x1 < x2 and y1 > y2:
            x_coordinate = x2
            for coordinate in range(y2, y1 + 1):
                coordinate_points[(x_coordinate, coordinate)] = coordinate_points.get((x_coordinate, coordinate), 0) + 1
                x_coordinate -= 1
        elif x1 > x2 and y1 < y2:
            y_coordinate = y2
            for coordinate in range(y1, y2 +1 ):
                coordinate_points[(coordinate, y_coordinate)] = coordinate_points.get((coordinate, y_coordinate), 0) + 1
                y_coordinate -= 1
        elif x1 > x2 and y1 > y2:
            y_coordinate = y2
            for coordinate in range(x2, x1 + 1):
                coordinate_points[(coordinate, y_coordinate)] = coordinate_points.get((coordinate, y_coordinate), 0) + 1
                y_coordinate += 1
   
    
    for amount in coordinate_points.values():
        if amount >= 2:
            count += 1
        
    return count


# print(get_vents_input())
# print(transform_vents_input())
print(get_coordinate_pairs())
# print(count_coordinate_points())


# 19424 too low
# 17107 too low
