def get_vents_input():
    with open("code_challenges/advent_of_code/vents_input") as vents_input:
        vents_coordinates = vents_input.read().split("\n")
        
    vents_coordinates = [vent_coordinate.split("->") for vent_coordinate in vents_coordinates]
    vents_coordinates = [coordinate.strip() for vent_coordinate in vents_coordinates for coordinate in vent_coordinate]
    vents_coordinates = [vent_coordinate.split(",") for vent_coordinate in vents_coordinates]

    return vents_coordinates


def mark_coordinates_horizontal_vertical():
    vents_coordinates = get_vents_input()
    coordinate_pairs = []
    biggest_x = 0
    biggest_y = 0
    j = 1
    i = 0
    for _ in range(len(vents_coordinates)):
        if j > len(vents_coordinates):
            break
        if vents_coordinates[i][0] == vents_coordinates[j][0] or vents_coordinates[i][1] == vents_coordinates[j][1]:
            coordinate_pairs.append([vents_coordinates[i], vents_coordinates[j]])
        i += 2
        j += 2
    coordinate_pairs = [[int(coordinate_x), int(coordinate_y)] for coordinate_pair in coordinate_pairs for coordinate_x, coordinate_y in coordinate_pair]
    for x, y in coordinate_pairs:
        if x > biggest_x:
            biggest_x = x
        if y > biggest_y:
            biggest_y = y
    coordinates_map = [[0 for i in range(biggest_x + 1)] for i in range(biggest_y + 1)]
    j = 1
    i = 0
    for _ in range(len(coordinate_pairs)):
        if j > len(coordinate_pairs):
            break
        if coordinate_pairs[i][1] == coordinate_pairs[j][1]:
            if coordinate_pairs[i][0] < coordinate_pairs[j][0]:
                for coordinate in range(coordinate_pairs[i][0], coordinate_pairs[j][0] + 1):
                    coordinates_map[coordinate_pairs[i][1]][coordinate] += 1
            else:      
                for coordinate in range(coordinate_pairs[j][0], coordinate_pairs[i][0] + 1):
                    coordinates_map[coordinate_pairs[i][1]][coordinate] += 1
        if coordinate_pairs[i][0] == coordinate_pairs[j][0]:
            if coordinate_pairs[j][1] < coordinate_pairs[i][1]:
                for coordinate in range(coordinate_pairs[j][1], coordinate_pairs[i][1] + 1):
                    coordinates_map[coordinate][coordinate_pairs[i][0]] += 1
            else:
                for coordinate in range(coordinate_pairs[i][1], coordinate_pairs[j][1] + 1):
                    coordinates_map[coordinate][coordinate_pairs[i][0]] += 1
        i += 2
        j += 2
            
    danger_zone = 0
    for coordinates in coordinates_map:
        for coordinate in coordinates:
            if coordinate >= 2:
                danger_zone += 1
    return danger_zone

def mark_coordinates_horizontal_vertical_diagonal():
    vents_coordinates = get_vents_input()
    coordinate_pairs = []
    i = 0
    j = 1
    for _ in range(len(vents_coordinates)):
        if j > len(vents_coordinates):
            break
        coordinate_pairs.append([vents_coordinates[i], vents_coordinates[j]])        
        i += 2
        j += 2
    biggest_x = 0
    biggest_y = 0
    coordinate_pairs = [[int(coordinate_x), int(coordinate_y)] for coordinate_pair in coordinate_pairs for coordinate_x, coordinate_y in coordinate_pair]
    for x, y in coordinate_pairs:
        if x > biggest_x:
            biggest_x = x
        if y > biggest_y:
            biggest_y = y
    coordinates_map = [[0 for i in range(biggest_x + 1)] for i in range(biggest_y + 1)]

    i = 0
    j = 1
    for _ in range(len(coordinate_pairs)):
        if j > len(coordinate_pairs):
            break
        if coordinate_pairs[i][1] == coordinate_pairs[j][1]:
            if coordinate_pairs[i][0] < coordinate_pairs[j][0]:
                for coordinate in range(coordinate_pairs[i][0], coordinate_pairs[j][0] + 1):
                    coordinates_map[coordinate_pairs[i][1]][coordinate] += 1
            else:      
                for coordinate in range(coordinate_pairs[j][0], coordinate_pairs[i][0] + 1):
                    coordinates_map[coordinate_pairs[i][1]][coordinate] += 1
        elif coordinate_pairs[i][0] == coordinate_pairs[j][0]:
            if coordinate_pairs[j][1] < coordinate_pairs[i][1]:
                for coordinate in range(coordinate_pairs[j][1], coordinate_pairs[i][1] + 1):
                    coordinates_map[coordinate][coordinate_pairs[i][0]] += 1
            else:
                for coordinate in range(coordinate_pairs[i][1], coordinate_pairs[j][1] + 1):
                    coordinates_map[coordinate][coordinate_pairs[i][0]] += 1
        elif coordinate_pairs[j][0] < coordinate_pairs[i][0] and coordinate_pairs[j][1] < coordinate_pairs[i][1]:   
            x_coordinate = coordinate_pairs[j][0]
            for coordinate in range(coordinate_pairs[j][1], coordinate_pairs[i][1] + 1):
                coordinates_map[coordinate][x_coordinate] += 1
                x_coordinate += 1
        elif coordinate_pairs[i][0] < coordinate_pairs[j][0] and coordinate_pairs[i][1] > coordinate_pairs[j][1]:
            x_coordinate = coordinate_pairs[j][0] 
            for coordinate in range(coordinate_pairs[j][1], coordinate_pairs[i][1] + 1):
                coordinates_map[coordinate][x_coordinate] += 1
                x_coordinate -= 1
        elif coordinate_pairs[i][0] < coordinate_pairs[j][0] and coordinate_pairs[i][1] < coordinate_pairs[j][1]:
            x_coordinate = coordinate_pairs[i][0]
            for coordinate in range(coordinate_pairs[i][0], coordinate_pairs[j][0] + 1):
                coordinates_map[coordinate][coordinate] += 1
        elif coordinate_pairs[j][0] < coordinate_pairs[i][0] and coordinate_pairs[j][1] > coordinate_pairs[i][1]:
            y_coordinate = coordinate_pairs[j][1] 
            for coordinate in range(coordinate_pairs[j][0], coordinate_pairs[i][0] + 1): 
                coordinates_map[coordinate][y_coordinate] += 1
                y_coordinate -= 1
        
        i += 2
        j += 2  
    danger_zone = 0
    for coordinates in coordinates_map:
        for coordinate in coordinates:
            if coordinate >= 2:
                danger_zone += 1


    return danger_zone

print(get_vents_input())
# print(mark_coordinates_horizontal_vertical())
# print(mark_coordinates_horizontal_vertical_diagonal())
#19424 too lovw