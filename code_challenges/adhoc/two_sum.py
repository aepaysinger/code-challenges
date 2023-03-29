def two_sum(numbers, target):

    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if i == j:
                continue
            if numbers[i] + numbers[j] == target:
                return [i, j]


if __name__ == "__main__":
    target = 6
    numbers = [3, 2, 4]
    print(two_sum(numbers, target))
