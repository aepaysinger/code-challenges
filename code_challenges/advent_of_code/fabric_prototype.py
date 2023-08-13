def get_elf_claims():
    with open("code_challenges/advent_of_code/elf_claims") as claims:
        elf_claims = claims.read().split("\n")
    return elf_claims


def break_down_claims_info():
    claims_info = get_elf_claims()
    claims_info = [claim.split(" ") for claim in claims_info]

    return claims_info


def organize_claim_info():
    claims_info = break_down_claims_info()

    claims = {}
    for claim in claims_info:
        x, y = claim[2].split(",")
        x_coordinate = int(x)
        y_coordinate = int(y[:-1])
        length, height = claim[3].split("x")

        claims[claim[0]] = [(x_coordinate, y_coordinate), (length, height)]

    return claims


def find_overlap():
    claims_info = organize_claim_info()
    coordinates = set()
    overlap = set()
    track_claims = {}

    for claim_number, (x_y_coordinates, length_height) in claims_info.items():
        x_coordinate = x_y_coordinates[0]
        length, height = length_height
        for x_coordinate in range(x_coordinate, x_coordinate + int(length)):
            y_coordinate = x_y_coordinates[1]
            while y_coordinate <= (int(height) + x_y_coordinates[1]) - 1:
                if (x_coordinate, y_coordinate) in coordinates:
                    overlap.add((x_coordinate, y_coordinate))
                else:
                    coordinates.add((x_coordinate, y_coordinate))
                track_claims[(x_coordinate, y_coordinate)] = (
                    track_claims.get((x_coordinate, y_coordinate), 0) + 1
                )
                y_coordinate += 1
    return len(overlap), track_claims


def find_no_overlap():
    claims_info = organize_claim_info()
    _, track_claims = find_overlap()
    for claim_number, (x_y_coordinates, length_height) in claims_info.items():
        x_coordinate = x_y_coordinates[0]
        length, height = length_height
        count = 0
        for x_coordinate in range(x_coordinate, x_coordinate + int(length)):
            y_coordinate = x_y_coordinates[1]
            while y_coordinate <= (int(height) + x_y_coordinates[1]) - 1:
                if track_claims[(x_coordinate, y_coordinate)] == 1:
                    count += 1
                y_coordinate += 1

            if count == int(length) * int(height):
                return claim_number
