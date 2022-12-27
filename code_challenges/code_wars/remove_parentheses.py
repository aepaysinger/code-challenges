class CharacterRemover:
    def __init__(self, characters):
        self.characters = characters
        self.start_item = "("
        self.stop_item = ")"

    def item_to_remove(self):
        start_item_index = None
        stop_item_index = None

        for i in range(len(self.characters)):
            if self.characters[i] == self.start_item:
                start_item_index = i
            elif self.characters[i] == self.stop_item:
                stop_item_index = i
                return start_item_index, stop_item_index

    def remove_item(self):
        start, stop = self.item_to_remove()
        self.characters = self.characters[:start] + self.characters[stop + 1 :]
        if self.start_item in self.characters and self.stop_item in self.characters:
            self.item_to_remove()
            self.remove_item()

        return self.characters


def remove_parentheses(characters):
    characters = CharacterRemover(characters)
    characters.item_to_remove()
    return characters.remove_item()


if __name__ == "__main__":
    characters = "this(is)it"
    print(remove_parentheses(characters))
