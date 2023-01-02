class FindString:
    def __init__(self, characters):
        self.characters = characters
        self.count = 0

    def find_hidden_characters(self, hidden_characters):
        j = len(hidden_characters)
        for i in range(len(self.characters)):
            if self.characters[i:j] == hidden_characters:
                self.count += 1
            j += 1
        return self.count


def find_string(characters, hidden_characters):
    find_string = FindString(characters)

    return find_string.find_hidden_characters(hidden_characters)


if __name__ == "__main__":
    characters = "I am an Indian, by birth."
    hidden_characters = "Birth"
    print(find_string(characters, hidden_characters))
