def first_non_repeating_letter(word):
    for letter in word:
        if word.find(letter):
            continue
        else:
            return letter



if __name__ == "__main__":
    word = "stress"
    print(first_non_repeating_letter(word))
