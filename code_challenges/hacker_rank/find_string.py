class FindString:
    def __init__(self, characters, hidden_characters):
        self.characters = characters
        self.hidden_characters = hidden_characters
        self.count = 0

    def find_hidden_characters(self):
        j = len(self.hidden_characters)
        for i in range(len(self.characters)):
            if self.characters[i:j] == self.hidden_characters:
                self.count += 1
            j += 1
        return self.count


def find_string(characters, hidden_characters):
    find_string = FindString(characters, hidden_characters)

    return find_string.find_hidden_characters()


if __name__ == "__main__":
    characters = "I am an Indian, by birth."
    hidden_characters = "Birth"
    print(find_string(characters, hidden_characters))
