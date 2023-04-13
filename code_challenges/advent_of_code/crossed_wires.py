def get_wires_path():

    with open("./code_challenges/advent_of_code/wires_input") as wires:
        wires_path = wires.read().split("\n\n")

    return wires_path


def find_wires_path():
    wires_path = get_wires_path()
    wire_a_moves = wires_path[0].split(",")
    wire_b_moves = wires_path[1].split(",")
    x_move = 0
    y_move = 0
    wire_a_steps = []
    wire_b_steps = []
    wire_a_x_points = {}
    wire_b_x_points = {}
    wire_a_y_points = {}
    wire_b_y_points = {}
    for move in wire_a_moves:
        if move[0] == "R":
            wire_a_y_points[y_move] = wire_a_y_points.get(x_move, []) + [
                (x_move, (int(move[1:]) + x_move))
            ]
            wire_a_steps.append((x_move, y_move))
            x_move += int(move[1:])
        elif move[0] == "U":
            wire_a_x_points[x_move] = wire_a_x_points.get(y_move, []) + [
                (y_move, (int(move[1:]) + y_move))
            ]
            wire_a_steps.append((x_move, y_move))
            y_move += int(move[1:])
        elif move[0] == "L":
            wire_a_y_points[y_move] = wire_a_y_points.get(x_move, []) + [
                (x_move, (x_move - int(move[1:])))
            ]
            wire_a_steps.append((x_move, y_move))
            x_move -= int(move[1:])
        elif move[0] == "D":
            wire_a_x_points[x_move] = wire_a_x_points.get(y_move, []) + [
                (y_move, (y_move - int(move[1:])))
            ]
            wire_a_steps.append((x_move, y_move))
            y_move -= int(move[1:])
    x_move = 0
    y_move = 0
    for move in wire_b_moves:
        if move[0] == "R":
            wire_b_y_points[y_move] = wire_b_y_points.get(y_move, []) + [
                (x_move, (int(move[1:]) + x_move))
            ]
            wire_b_steps.append((x_move, y_move))
            x_move += int(move[1:])
        elif move[0] == "U":
            wire_b_x_points[x_move] = wire_b_x_points.get(y_move, []) + [
                (y_move, int(move[1:]) + y_move)
            ]
            wire_b_steps.append((x_move, y_move))
            y_move += int(move[1:])
        elif move[0] == "L":
            wire_b_y_points[y_move] = wire_b_y_points.get(x_move, []) + [
                (x_move, (x_move - int(move[1:])))
            ]
            wire_b_steps.append((x_move, y_move))
            x_move -= int(move[1:])
        elif move[0] == "D":
            wire_b_x_points[x_move] = wire_b_x_points.get(y_move, []) + [
                (y_move, (y_move - int(move[1:])))
            ]
            wire_b_steps.append((x_move, y_move))
            y_move -= int(move[1:])
    return wire_a_x_points, wire_a_y_points, wire_b_x_points, wire_b_y_points, wire_a_steps, wire_b_steps


def find_where_wires_cross():
    (
        wire_a_x_points,
        wire_a_y_points,
        wire_b_x_points,
        wire_b_y_points,
        wire_a_steps,
        wire_b_steps
    ) = find_wires_path()
    y_range_start = None
    y_range_end = None
    x_range_start = None
    y_range_end = None
    pairs_to_check = []

    for y_points in wire_b_y_points:
        for pairs in wire_b_y_points[y_points]:
            y_range_start = pairs[0] if pairs[0] < pairs[1] else pairs[1]
            y_range_end = pairs[1] if pairs[0] < pairs[1] else pairs[0]
            for x_points in wire_a_x_points:
                if x_points in range(y_range_start, y_range_end):
                    for pairs in wire_a_x_points[x_points]:
                        print(pairs, wire_a_x_points, x_points, wire_a_x_points[x_points])
                        x_range_start = pairs[0] if pairs[0] < pairs[1] else pairs[1]
                        x_range_end = pairs[1] if pairs[0] < pairs[1] else pairs[0]
                    if y_points in range(x_range_start, x_range_end):
                        pairs_to_check.append((x_points, y_points))

    for y_points in wire_a_y_points:
        for pairs in wire_a_y_points[y_points]:
            if pairs[0] < pairs[1]:
                y_range_start = pairs[0]
                y_range_end = pairs[1]
            else:
                y_range_start = pairs[1]
                y_range_end = pairs[0]
            for x_points in wire_b_x_points:
                if x_points in range(y_range_start, y_range_end):
                    for pairs in wire_b_x_points[x_points]:
                        if pairs[0] < pairs[1]:
                            x_range_start = pairs[0]
                            x_range_end = pairs[1]
                        else:
                            x_range_start = pairs[1]
                            x_range_end = pairs[0]
                    if y_points in range(x_range_start, x_range_end):
                        if x_points == 0 and y_points == 0:
                            continue
                        pairs_to_check.append((x_points, y_points))

    return pairs_to_check


def find_closest_to_starting_point():
    pairs_to_check = find_where_wires_cross()

    distance = float("inf")

    for pairs in pairs_to_check:
        x_pairs = abs(pairs[0])
        y_pairs = abs(pairs[1])

        if x_pairs + y_pairs < distance:
            distance = x_pairs + y_pairs

    return distance


# print(find_wires_path())
print(find_where_wires_cross())
