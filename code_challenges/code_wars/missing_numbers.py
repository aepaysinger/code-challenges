class MissingNumbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def organize(self):
        self.numbers = sorted(self.numbers)
        last_number = self.numbers[-1]

        return self.numbers, last_number

    def fill_in_the_gaps(self):
        numbers, last_number = self.organize()
        the_gaps = []
        for i in range(last_number - 1):
            if i == last_number:
                break
            if numbers[i + 1] == numbers[i] + 1:
                continue
            else:
                numbers.insert(i + 1, numbers[i] + 1)
                the_gaps.append(numbers[i] + 1)

        return the_gaps

def find_missing_numbers(numbers):
    missing_numbers = MissingNumbers(numbers)
    missing_numbers.organize()

    return missing_numbers.fill_in_the_gaps()

if __name__ == "__main__":
    numbers = [2, 3, 1, 9, 4, 5, 6, 10, 7]
    print(find_missing_numbers(numbers))


