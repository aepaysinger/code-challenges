from copy import deepcopy


class MissingNumbers:
    def __init__(self, numbers):
        self.numbers = numbers
        self.numbers_ = deepcopy(numbers)

    def organize(self):
        self.numbers = sorted(self.numbers)
        last_number = self.numbers[-1]

        return self.numbers, last_number

    def fill_in_the_gaps(self):
        numbers, last_number = self.organize()
        the_gaps = []
        for i in range(last_number - 1):
            print(i, i+1, len(numbers)-1)
            
            if numbers[i + 1] == numbers[i] + 1:
            # print(i, numbers)
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
    numbers_ = [5, 4, 2, 9, 3, 8, 10, 6, 7]
            #  [9, 10, 7, 2, 11, 8, 1, 17, 6, 16, 18, 19, 15, 3, 13]
    print(find_missing_numbers(numbers_))


