def first_non_repeating_letter(word):
    word = list(word)
    for i, letter in enumerate(word):
        if letter not in word[i + 1 :: 1] or letter not in word[0:i]:
            return letter


if __name__ == "__main__":
    word = "abcdabcde"
    print(first_non_repeating_letter(word))
