def spreadsheet_input():
    with open(
        "./code_challenges/advent_of_code/spreadsheet_input"
    ) as numbers:
        spread_sheet = numbers.read().split("\t")
    spread_sheet_numbers = []
    holding = []
    for numbers in spread_sheet:
        if "\n" in numbers:
            numbers = numbers.split("\n")
            holding.append(int(numbers[0]))
            spread_sheet_numbers.append(holding)
            holding = [int(numbers[1])]            
        else:
            holding.append(int(numbers))
    spread_sheet_numbers.append(holding)
    return spread_sheet_numbers

def checksum():
    spread_sheet_numbers = spreadsheet_input()
    sums = []
    for row in spread_sheet_numbers:
        biggest_number = 0
        smallest_number = float('inf')
        for number in row:
            if number > biggest_number:
                biggest_number = number
            elif number < smallest_number:
                smallest_number = number
        sums.append(biggest_number - smallest_number)

    return sum(sums)


def evenly_divisible_values():
    spread_sheet_numbers = spreadsheet_input()
    sums = []
    for row in spread_sheet_numbers:
        for number in row:
            start = 0
            for i in range(start, len(row)-1):
                if number % row[i + 1] == 0 and number != row[i+1]:
                    print(number, row[i+1])
                    sums.append(number//row[i + 1])
            start += 1
    return sum(sums)








    

# print(spreadsheet_input())
# print(checksum())
print(evenly_divisible_values())