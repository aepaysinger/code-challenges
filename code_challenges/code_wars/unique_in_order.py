class UniqueOrder:
    def __init__(self, sequence):
        self.sequence = sequence

    def pull_out_unique_character(self):
        unique_sequence = []
        unique_character = None
        for character in self.sequence:
            if character != unique_character:
                unique_sequence.append(character)
                unique_character = character
        return unique_sequence


def unique_in_order(sequence):
    find_unique_order = UniqueOrder(sequence)

    return find_unique_order.pull_out_unique_character()


if __name__ == "__main__":
    sequence = "AAAABBBCCDAABBB"
    print(unique_in_order(sequence))
