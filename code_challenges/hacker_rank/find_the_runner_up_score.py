def check_tie(array):
    return len(set(array)) == 1


def runner_up(array):
    if check_tie(array) == True:
        return "it's a tie!"
    else:
        biggest_number = -100
        second_biggest = -100
        for number in array:
            if number > biggest_number:
                second_biggest = biggest_number
                biggest_number = number
            elif number > second_biggest and number < biggest_number:
                second_biggest = number
    return second_biggest


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    print(runner_up(arr))
