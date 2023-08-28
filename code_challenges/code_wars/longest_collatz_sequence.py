def find_collatz_sequence(numbers):
    numbers_with_sequence = {}
    for number in numbers:
        numbers_with_sequence[number] = []
        updated_number = number
        while updated_number > 1:
            updated_number = collatz_number(updated_number)
            numbers_with_sequence[number].append(updated_number)
    return numbers_with_sequence


def collatz_number(num):
    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1


def find_longest_length(numbers):
    numbers_with_sequence = find_collatz_sequence(numbers)
    winner = 0
    winner_length = 0
    for number in numbers:
        if len(numbers_with_sequence[number]) > winner_length:
            winner = number
            winner_length = len(numbers_with_sequence[number])
    return winner
