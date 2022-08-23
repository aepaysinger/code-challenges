def move_zeros(lst):
    no_zeros = []
    zeros = []
    for number in lst:
        if number == 0:
            zeros.append(0)
        else:
            no_zeros.append(number)
    return no_zeros + zeros


if __name__ == "__main__":
    numbers = [1, 0, 1, 2, 0, 1, 3]
    print(move_zeros(numbers))
