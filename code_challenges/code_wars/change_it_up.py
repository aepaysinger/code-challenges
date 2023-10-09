class ChangeItUp:
    def __init__(self, text):
        self.text = text
        self.vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        self.morphed_text = ""

    def change_letter(self):
        for character in self.text:
            if character.isalpha():
                if character == "z" or character == "Z":
                    self.morphed_text += "a"
                else:
                    self.morphed_text += chr(ord(character) + 1)
            else:
                self.morphed_text += character
        return self.morphed_text

    def capitaliz_vowel(self):
        for character in self.morphed_text:
            if character in self.vowels:
                self.morphed_text = self.morphed_text.replace(
                    character, character.capitalize()
                )

        return self.morphed_text

    def lower_consonant(self):
        for character in self.morphed_text:
            if character not in self.vowels:
                self.morphed_text = self.morphed_text.replace(
                    character, character.lower()
                )
        return self.morphed_text


def changer(text):
    change_it = ChangeItUp(text)
    change_it.change_letter()
    change_it.capitaliz_vowel()

    return change_it.lower_consonant()


if __name__ == "__main__":
    text = "Hello World"
    print(changer(text))
