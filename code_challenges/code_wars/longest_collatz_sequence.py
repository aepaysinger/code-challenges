def find_collatz_sequence(numbers):
    numbers_with_sequence = []
    for number in numbers:
        pairs = [number, 0]
        updated_number = number
        while updated_number > 1:
            updated_number = collatz_number(updated_number)
            pairs[1] += 1
        numbers_with_sequence.append(pairs)
    return numbers_with_sequence


def collatz_number(num):
    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1


def find_longest_length(numbers):
    numbers_with_sequence = find_collatz_sequence(numbers)
    return max(numbers_with_sequence, key=lambda x: x[1])[0]
