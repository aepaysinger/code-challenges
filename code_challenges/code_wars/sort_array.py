def sort_array(numbers_to_sort):
    odds = iter(sorted(number for number in numbers_to_sort if number % 2))
    return [next(odds) if number % 2 else number for number in numbers_to_sort]
