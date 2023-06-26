def sum_of_the_smallest(numbers):
    smallest = None
    second_smallest = None
    for number in numbers:
        if number > 0:
            if smallest is None or number < smallest:
                second_smallest = smallest
                smallest = number
            elif second_smallest is None or number < second_smallest:
                second_smallest = number
    if smallest and second_smallest:
        return smallest + second_smallest


if __name__ == "__main__":
    numbers = [5, 1, 7, 9, 3, 2]
    print(sum_of_the_smallest(numbers))
