def is_valid_coordinates(coordinates):
    for character in coordinates:
        if character.isalpha():
            return False
    x_y_coordinates = coordinates.split(", ")
    try:
        x_coordinate = float(x_y_coordinates[0])
        y_coordinate = float(x_y_coordinates[1])
    except:
        return False

    if len(x_y_coordinates) > 2:
        return False
    if -90 <= x_coordinate <= 90.00 and -180 <= y_coordinate <= 180.00:
        return True
    return False


if __name__ == "__main__":
    coordinates = "24.53525235, 23.45235"
    print(is_valid_coordinates(coordinates))
