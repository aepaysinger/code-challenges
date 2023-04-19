def decode_morse(morse_code):
    translator = {
        "": "",
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        ".-.-.-": ".",
        "--..--": ",",
        "..--..": "?",
        ".----.": "'",
        "-.-.--": "!",
        "-..-.": "/",
        "-.--.": "(",
        "-.--.-": ")",
        ".-...": "&",
        "---...": ":",
        "-.-.-.": ";",
        "-...-": "=",
        ".-.-.": "+",
        "-....-": "-",
        "..--.-": "_",
        ".-..-.": '"',
        "...-..-": "$",
        ".--.-.": "@",
        "...---...": "SOS",
    }
    translation = ""
    morse_code = morse_code.split(" ")

    # for i in range(len(morse_code) - 1, -1, -1):
    #     if morse_code[i] == "":
    #         continue
    #     else:
    #         morse_code = morse_code[: i + 1]
    #         break
    print(morse_code)
    # for i, character in enumerate(morse_code):
    #     if character == "" and morse_code[i + 1] == "" and len(translation) > 0:
    #         translation += " "
    #     else:
    #         translation += translator[character]
    # return translation.strip()
    for i in range(len(morse_code) + 1):
        if morse_code[i] == "" and morse_code[i + 1] == "" and len(translation) > 0:
            translation += " "
        else:
            translation += translator[morse_code[i]]
    return translation.strip()


if __name__ == "__main__":
    morse_code = "      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.- "
    print(decode_morse(morse_code))
