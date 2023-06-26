class PersistentMultiplication:
    def __init__(self, number):
        self.number = number
        self.count = 0

    def break_up_numbers(self):
        self.numbers = [int(x) for x in str(self.number)]

        return self.numbers

    def multiply_numbers(self):
        if len(self.numbers) == 1:
            return 0
        total = 1
        for i in range(len(self.numbers)):
            total *= self.numbers[i]
        self.count += 1
        total = [int(x) for x in str(total)]
        self.numbers = total
        if len(self.numbers) > 1:
            self.multiply_numbers()

        return self.count


def persistence(number):
    persistant_numbers = PersistentMultiplication(number)
    persistant_numbers.break_up_numbers()

    return persistant_numbers.multiply_numbers()


if __name__ == "__main__":
    number = 25
    print(persistence(number))
