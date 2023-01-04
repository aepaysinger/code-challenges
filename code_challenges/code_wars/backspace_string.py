class Backspace:
    def __init__(self, characters):
        self.characters = characters

    def hit_backspace(self):
        index_to_remove = self.characters.find("#")
        while index_to_remove != -1:
            if index_to_remove == 0:
                self.characters = self.characters[1:]
            else:
                self.characters = self.characters[:index_to_remove - 1] + self.characters[index_to_remove + 1:]
            index_to_remove = self.characters.find("#")    
        
        return self.characters


def backspace_string(characters):
    the_string = Backspace(characters)
    return the_string.hit_backspace()


if __name__ == "__main__":
    characters = "abc#d##c"
    print(backspace_string(characters))
