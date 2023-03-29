def to_nato(words):
    translator = {
        "A": "Alfa",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "Xray",
        "Y": "Yankee",
        "Z": "Zulu",
    }
    translation = ""
    for word in words:
        if word.isalpha():
            for letter in word:
                translation += translator[letter.upper()] + " "
        elif word == " ":
            continue
        else:
            translation += word + " "

    return translation[:-1]


if __name__ == "__main__":
    words = input()
    print(to_nato(words))
