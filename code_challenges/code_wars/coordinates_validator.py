def is_valid_coordinates(coordinates):
    for character in coordinates:
        if character.isalpha():
            return False
    try:
        x_coordinate = float(coordinates.split(", ")[0])
        y_coordinate = float(coordinates.split(", ")[1])
    except:
        return False
    if len(list(coordinates.split(","))) > 2:
        return False
    if -90 <= x_coordinate <= 90.00 and -180 <= y_coordinate <= 180.00:
        return True
    return False


if __name__ == "__main__":
    coordinates = "1e1, 1e1"
    print(is_valid_coordinates(coordinates))
