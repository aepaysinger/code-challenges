def first_non_repeating_letter(word):
    word = list(word)
    for i, letter in enumerate(word):
        if letter in word[i + 1 :: 1] or letter in word[0:i]:
            print(letter, word[i + 1 :: 1], word[0:i])
            continue
        else:
            return letter


if __name__ == "__main__":
    word = "abcdabcde"
    print(first_non_repeating_letter(word))
