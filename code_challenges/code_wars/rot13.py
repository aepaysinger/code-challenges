def rot13(a_string):
    code = ""
    amount_to_shift = 13
    upper_alpha_min = 65
    upper_alpha_max = 90
    lower_alpha_min = 97
    lower_alpha_max = 122
    for character in a_string:
        if character.isalpha():
            count = ord(character) + amount_to_shift
            if character.islower():
                if count > lower_alpha_max:
                    new = count - lower_alpha_max
                    code += chr((lower_alpha_min + 1) + new)
                else:
                    code += chr(count)
            else:
                if count > upper_alpha_max:
                    new = count - upper_alpha_max
                    code += chr((upper_alpha_min + 1) + new)
                else:
                    code += chr(count)
        else:
            code += character
    return code


if __name__ == "__main__":
    a_string = "test"
    print(rot13(a_string))
