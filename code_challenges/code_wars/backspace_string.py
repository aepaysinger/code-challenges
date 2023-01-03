class Backspace:
    def __init__(self, characters):
        self.characters = characters

    def hit_backspace(self):
        while "#" in self.characters:
            for i, character in enumerate(self.characters):
                if character == "#":
                    if i == 0:
                        self.characters = self.characters[1:]
                        break
                    else:
                        self.characters = (
                            self.characters[: i - 1] + self.characters[i + 1 :]
                        )
                        break

        return self.characters


def backspace_string(characters):
    the_string = Backspace(characters)
    return the_string.hit_backspace()


if __name__ == "__main__":
    characters = "abc####d##c#"
    print(backspace_string(characters))
