def find_highest_substring_value(strings):
    alphabet = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }

    highest_substring_value = 0
    substring_value = 0
    for string in strings:
        for character in string:
            substring_value += alphabet[character]
        if substring_value > highest_substring_value:
            highest_substring_value = substring_value
        substring_value = 0

    return highest_substring_value


def find_substrings(string):
    sub_strings = []
    sub_string = []
    vowels = ("a", "e", "i", "o", "u")
    for i, character in enumerate(string):
        if i == len(string) - 1:
            if character not in vowels:
                sub_string.append(character)
                sub_strings.append(sub_string)
            else:
                sub_strings.append(sub_string)
        elif character not in vowels:
            sub_string.append(character)

        else:
            if len(sub_string) == 0:
                continue
            else:
                sub_strings.append(sub_string)
                sub_string = []
    return sub_strings
