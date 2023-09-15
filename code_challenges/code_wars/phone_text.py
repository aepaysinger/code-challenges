def presses(phrase):
    key_pad_touches = {
        1: {"A", "D", "G", "J", "M", "P", "T", "W", " ", "*", "#", "1"},
        2: {"B", "E", "H", "K", "N", "Q", "U", "X", "0"},
        3: {"C", "F", "I", "L", "O", "R", "V", "Y"},
        4: {"2", "3", "4", "5", "6", "S", "8", "Z"},
        5: {"7", "9"},
    }
    number_of_touches = 0
    for character in phrase.upper():
        for presses, characters in key_pad_touches.items():
            if character in characters:
                number_of_touches += presses
    return number_of_touches
