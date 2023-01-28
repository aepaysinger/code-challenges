class EqualSumSidesArray:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_sides_of_array(self):
        left_side = 0
        right_side = None

        if sum(self.numbers[1:]) == left_side:
            return 0
        if len(self.numbers) == 2 and self.numbers[0] == 0:
            return 1

        j = 2
        for i in range(len(self.numbers)):
            left_side = sum(self.numbers[: i + 1])
            right_side = sum(self.numbers[j:])
            if left_side == right_side:
                return i + 1
            j += 1
            if j > len(self.numbers):
                break
        return -1


def find_even_index(numbers):
    equal_sides = EqualSumSidesArray(numbers)

    return equal_sides.sum_sides_of_array()


if __name__ == "__main__":
    numbers = [0, 20, 72, -17, -11, 20, 59, -17]
    print(find_even_index(numbers))
