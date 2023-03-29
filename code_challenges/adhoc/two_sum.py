def two_sum(numbers, target):
    lookup = {}
    for i, num in enumerate(numbers):
        if target - num in lookup:
            return [lookup[target - num], i ]
        lookup[num] = i

if __name__ == "__main__":
    target = 6
    numbers = [3, 3, 1, 8, 7, 4]
    print(two_sum(numbers, target))
