class FindOddInt:
    def __init__(self, numbers):
        self.numbers = numbers
        self.numbers_amount = {}

    def set_numbers_amount(self):
        for number in self.numbers:
            self.numbers_amount[number] = self.numbers_amount.get(number, 0) + 1

    def find_odd_int(self):
        for number in self.numbers_amount:
            if self.numbers_amount[number] % 2 != 0:
                return number


def finding_odd_int(seq):
    finding_odd_int = FindOddInt(seq)
    finding_odd_int.set_numbers_amount()

    return finding_odd_int.find_odd_int()


if __name__ == "__main__":
    seq = [1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]
    print(finding_odd_int(seq))
