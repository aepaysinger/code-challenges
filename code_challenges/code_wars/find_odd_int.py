class FindOddInt():
    def __init__(self, numbers):
        self.numbers = numbers
        self.number_amount = {}

    
    def find_amount(self):
        for number in self.numbers:
            self.number_amount[number] = self.number_amount.get(number, 0) + 1

        for number in self.number_amount:
            if self.number_amount[number] % 2 != 0:
                return number


# def find_it(seq):
#     number_amount = {}
#     for number in seq:
#         number_amount[number] = number_amount.get(number, 0) +1

#     for number in number_amount:
#         if number_amount[number] % 2 != 0:
#             return number

    
# if __name__ == "__main__":
#     seq = [1,1,1,1,1,1,10,1,1,1,1]
#     print(find_it(seq))