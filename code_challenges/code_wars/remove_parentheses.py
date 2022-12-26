class CharacterRemover:
    def __init__(self,  characters):
        self.characters = characters

    def item_to_remove(self):
        self.start_item = "("
        start_item_index = None
        self.stop_item = ")"
        stop_item_index = None
        
        for i in range(len(self.characters)):
            if self.characters[i] == self.start_item:
                start_item_index = i
            elif self.characters[i] == self.stop_item:
                stop_item_index = i
                print(start_item_index, stop_item_index)
                return start_item_index, stop_item_index

    def remove_item(self):
        print(self.item_to_remove)
        start, stop = self.item_to_remove()
        self.characters = self.characters[:start] + self.characters[stop + 1:]
        
        return self.characters

    def final_check(self):
        self.characters = self.remove_item()
        if self.start_item in self.characters and self.stop_item in self.characters:
            self.remove_item()
        
        return self.characters

def remove_parentheses(characters):
    characters = CharacterRemover(characters)
    characters.item_to_remove()
    characters.remove_item()
    return characters.final_check()


if __name__ == "__main__":
    characters = "example(unwanted thing)example"
    print(remove_parentheses(characters))