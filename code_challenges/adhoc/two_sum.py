def two_sum(numbers, target):
    j = len(numbers) - 1
    numbers.sort()
    for i in numbers:
        while numbers[i] + numbers[j] > target:
            j -= 1
        if numbers[i] + numbers[j] < target:
            continue
        if numbers[i] + numbers[j] == target:
            result = [i, j]
            result.sort()
            return result


if __name__ == "__main__":
    target = 6
    numbers = [3, 3, 1, 8, 7, 4]
    print(two_sum(numbers, target))
