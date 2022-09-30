from collections import Counter


def first_non_repeating_letter(word):
    counter = Counter(word)
    for letter in word:
        if counter[letter] == 1:
            return letter


if __name__ == "__main__":
    word = "abcdabcde"
    print(first_non_repeating_letter(word))
