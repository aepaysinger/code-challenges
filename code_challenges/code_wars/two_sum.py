def two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
