class MultiplicationTable:
    def __init__(self, size):
        self.size = size

    def build_table(self):
        table = []
        for number in range(1, self.size + 1):
            number_set = []
            set_number = number
            for _ in range(self.size):
                number_set.append(number)
                number += set_number
            table.append(number_set)

        return table


def multiplication_table(size):
    the_table = MultiplicationTable(size)
    return the_table.build_table()


if __name__ == "__main__":
    size = 5
    print(multiplication_table(size))
