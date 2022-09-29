# takes a string, has a method find(takes a substring) - will tell you the index
# of the starting position of the substring withing the string or -1 if not in string
class LookUp:
    def __init__(self, text):
        self.text = text

    def find(self, sub_text):
        for i in range(len(self.text) - len(sub_text) + 1):
            if sub_text == self.text[i : len(sub_text) + i]:
                return i
        return -1
