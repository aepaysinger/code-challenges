def digits_input():
    with open(
        "./code_challenges/advent_of_code/digits_input"
    ) as csequence_of_digits:
        digits = csequence_of_digits.read()
    return [int(digit) for digit in digits]

def check_to_add_next_digit():
    digits = digits_input()
    total = 0
    for i, digit in enumerate(digits):
        if i == len(digits) - 1 and digit == digits[0]:
            total += digit
        elif i == len(digits) - 1 and digit != digits[0]:
            break
        elif digit == digits[i +1]:
            total += digit
    return total


def check_to_add_halfway_digit():
    digits = digits_input()
    half_way = len(digits)//2
    extra_digits = digits * len(digits)
    total = 0
    for i, digit in enumerate(digits):
        if i == len(digits) - 1 and digits == digits[half_way - 1]:
            total += digit
        elif digit == extra_digits[i + half_way]:
            total += digit
    return total
