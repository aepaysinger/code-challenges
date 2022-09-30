from collections import Counter


def first_non_repeating_letter(word):
    for letter in word:
        if Counter(word)[letter] == 1:
            return letter 


if __name__ == "__main__":
    word = "abcdabcde"
    print(first_non_repeating_letter(word))
