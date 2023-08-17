def find_highest_substring_value(strngs):
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
    for strng in strngs:
        for character in strng:
            substring_value += alphabet[character]
        if substring_value > highest_substring_value:
            highest_substring_value = substring_value
        substring_value = 0

    return highest_substring_value


def find_substrings(strng):
    sub_strngs = []
    sub_strng = []
    vowels = ("a", "e", "i", "o", "u")
    for i, character in enumerate(strng):
        if i == len(strng) - 1:
            if character not in vowels:
                sub_strng.append(character)
                sub_strngs.append(sub_strng)
            else:
                sub_strngs.append(sub_strng)
        elif character not in vowels:
            sub_strng.append(character)

        else:
            if len(sub_strng) == 0:
                continue
            else:
                sub_strngs.append(sub_strng)
                sub_strng = []
    return sub_strngs
