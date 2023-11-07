from collections import Counter


class UniqueNumber:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_unique(self):
        unique_numbers = Counter(self.numbers)
        for number in unique_numbers:
            if unique_numbers[number] == 1:
                return number


def find_unique_number(numbers):
    unique = UniqueNumber(numbers)

    return unique.find_unique()


if __name__ == "__main__":
    numbers = [1, 1, 1, 2, 1, 1]
    print(find_unique_number(numbers))
