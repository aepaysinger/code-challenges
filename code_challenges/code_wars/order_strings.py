class OrderStrings:
    def __init__(self, text):
        self.text = text
        self.split_text = text.split(" ")
        self.position_in_string = {}

    def find_the_number(self):
        position = 0
        for item in self.split_text:
            for i in range(len(item)):
                if item[i].isdigit():
                    self.position_in_string[position] = int(item[i]) - 1
                    position += 1
        return self.position_in_string

    def build_updated_order_string(self):
        placement = 0
        ordered_string = ""
        while len(ordered_string) < len(self.text):
            for key, value in self.position_in_string.items():
                if value == placement:
                    ordered_string += self.split_text[key] + " "

                    placement += 1

        return ordered_string[:-1]


def order(text):
    changed_order = OrderStrings(text)
    changed_order.find_the_number()

    return changed_order.build_updated_order_string()


if __name__ == "__main__":
    text = "is2 Thi1s T4est 3a"
    print(order(text))
