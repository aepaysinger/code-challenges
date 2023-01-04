class PersistentMultiplication:
    def __init__(self, numbers):
        self.numbers = numbers
        self.count = 0

    def break_up_numbers(self):
        self.numbers = [self.numbers]
        self.numbers = [
            int(x) if x.isdigit() else x for z in self.numbers for x in str(z)
        ]

        return self.numbers

    def multiply_numbers(self):
        if len(self.numbers) == 1:
            return 0

        total = [self.numbers[0]]
        for i in range(1, len(self.numbers)):
            total[0] *= self.numbers[i]
        self.count += 1
        total = [int(x) if x.isdigit() else x for z in total for x in str(z)]
        self.numbers = total
        if len(self.numbers) > 1:
            self.multiply_numbers()

        return self.count


def persistence(numbers):
    persistant_numbers = PersistentMultiplication(numbers)
    persistant_numbers.break_up_numbers()

    return persistant_numbers.multiply_numbers()


if __name__ == "__main__":
    numbers = 25
    print(persistence(numbers))
