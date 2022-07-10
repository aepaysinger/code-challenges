def runner_up(array):
    biggest_number = -100
    second_biggest = -100
    for number in array:
        if number > biggest_number:
            second_biggest = biggest_number
            biggest_number = number
        elif number > second_biggest and number < biggest_number:
            second_biggest = number
    print(second_biggest)


if __name__ == '__main__':
    # n = 8 8 8 8
    # arr = map(int, input().split())
    runner_up([8, 8, 8, 8])