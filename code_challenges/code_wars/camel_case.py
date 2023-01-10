class CamelCase:
    def __init__(self, words):
        self.words = words

    def change_case(self):
        seperated_words = self.words.split()
        case_changed_words = []
        for word in seperated_words:
            if word[0].islower():
                case_changed_words.append(word[0].upper() + word[1:])
        return case_changed_words

    def bring_words_together(self):
        case_changed_words = self.change_case()
        camel_case_words = "".join(case_changed_words)

        return camel_case_words


def camel_case(words):
    camel_it = CamelCase(words)

    return camel_it.bring_words_together()


if __name__ == "__main__":
    words = "hello case"
    print(camel_case(words))
