def decipher_this(code):
    words_to_decode = list(code.split(" "))
    deciphered_code = ""
    for word in words_to_decode:
        number = ""
        letters = ""
        for character in word:
            if character.isdigit():
                number += character
            else:
                letters += character
        word = word.replace(number, "")

        number = chr(int(number))
        if len(word) == 0:
            deciphered_code += number + " "
        elif len(word) == 1:
            deciphered_code += number + word + " "
        elif len(word) == 2:
            deciphered_code += number + word[-1] + word[0] + " "
        else:
            deciphered_code += number + word[:0] + word[-1] + word[1:-1] + word[0] + " "

    return deciphered_code[:-1]


if __name__ == "__main__":
    code = "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"

    print(decipher_this(code))
