class Backspace:
    def __init__(self, characters):
        self.characters = characters

    def hit_backspace(self):
        while "#" in self.characters:
            if self.characters.find("#") == 0:
                self.characters = self.characters[1:]
            else:
                self.characters = self.characters[:(self.characters.find("#")) - 1] + self.characters[(self.characters.find("#")) + 1:]
        
        return self.characters


def backspace_string(characters):
    the_string = Backspace(characters)
    return the_string.hit_backspace()


if __name__ == "__main__":
    characters = "abc#d##c"
    print(backspace_string(characters))
