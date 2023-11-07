def spreadsheet_input():
    with open("./code_challenges/advent_of_code/spreadsheet_input") as numbers:
        spread_sheet = numbers.read()

    spread_sheet_numbers = [
        [int(num) for num in row.split("\t")] for row in spread_sheet.split("\n")
    ]

    return spread_sheet_numbers


def checksum():
    spread_sheet_numbers = spreadsheet_input()
    sums = []
    for row in spread_sheet_numbers:
        biggest_number = 0
        smallest_number = float("inf")
        for i, number in enumerate(row):
            if number > biggest_number:
                if biggest_number < smallest_number and i != 0:
                    smallest_number = biggest_number
                biggest_number = number
            elif number < smallest_number:
                smallest_number = number
        sums.append(biggest_number - smallest_number)

    return sum(sums)


def evenly_divisible_values():
    spread_sheet_numbers = spreadsheet_input()
    sums = []
    for row in spread_sheet_numbers:
        for i, dividend in enumerate(row):
            for j, divisor in enumerate(row):
                if i != j and dividend % divisor == 0:
                    print(dividend, divisor)
                    sums.append(dividend // divisor)
    return sum(sums)
