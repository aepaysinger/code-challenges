def find_collatz_sequence(numbers):
    numbers_with_sequence = {}
    for number in numbers:
        numbers_with_sequence[number] = 0
        updated_number = number
        while updated_number > 1:
            updated_number = collatz_number(updated_number)
            numbers_with_sequence[number] += 1
    return numbers_with_sequence


def collatz_number(num):
    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1


def find_longest_length(numbers):
    return max(
        find_collatz_sequence(numbers), key=lambda x: find_collatz_sequence(numbers)[x]
    )
