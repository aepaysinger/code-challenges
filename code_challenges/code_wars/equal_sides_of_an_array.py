class EqualSumSidesArray:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_sides_of_array(self):
        right_total = sum(self.numbers)
        left_total = 0
        for i, number in enumerate(self.numbers):
            right_total -= number
            if right_total == left_total:
                return i
            left_total += number
        return -1


def find_even_index(numbers):
    equal_sides = EqualSumSidesArray(numbers)

    return equal_sides.sum_sides_of_array()


if __name__ == "__main__":
    numbers = [0, 20, 72, -17, -11, 20, 59, -17]
    print(find_even_index(numbers))
