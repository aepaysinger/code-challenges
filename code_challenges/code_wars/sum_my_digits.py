def sum_my_digits(starting_number, pattern, stop):
    digit_to_sum = str(get_number_list(starting_number, pattern, stop))
    digit_broken_up = []
    for digit in digit_to_sum:
        digit_broken_up.append(int(digit))
    return sum(digit_broken_up)


def get_number_list(starting_number, pattern, stop):
    number_list = [starting_number]
    while len(number_list) < stop:
        for i, number in enumerate(pattern):
            number_list.append(number_list[-1] + number)
    return number_list[stop - 1]


if __name__ == "__main__":
    starting_number = 10
    pattern = [2, 2, 5, 8]
    stop = 6
    print(sum_my_digits(starting_number, pattern, stop))
