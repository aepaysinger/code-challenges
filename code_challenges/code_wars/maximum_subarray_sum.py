def max_sequence(sequence):
    current_sum = 0
    max_sum = 0
    for number in sequence:
        current_sum = max(number, number + current_sum)
        max_sum = max(current_sum, max_sum)
    return max_sum


if __name__ == "__main__":
    sequence = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sequence(sequence))
