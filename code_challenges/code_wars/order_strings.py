class OrderStrings:
    def __init__(self, text):
        self.text = text
        self.split_text = text.split(" ")

    def sort_text(self):
        return " ".join(sorted(self.split_text, key=self.find_position))

    def find_position(self, characters):
        for character in characters:
            if character.isdigit():
                return int(character)


def order(text):
    changed_order = OrderStrings(text)

    return changed_order.sort_text()


if __name__ == "__main__":
    text = "T4est is2 Thi1s 3a"
    print(order(text))
