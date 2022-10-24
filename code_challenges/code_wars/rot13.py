def rot13(a_string):
    code = ""
    for character in a_string:
        if character.isalpha():
            count = ord(character) + 13
            if character.islower():
                if count > 122:
                    new = count - 122
                    code += chr(96 + new)
                else:
                    code += chr(count)
            else:
                if count > 90:
                    new = count - 90
                    code += chr(64 + new)
                else:
                    code += chr(count)
        else:
            code += character
    return code


if __name__ == "__main__":
    a_string = "test"
    print(rot13(a_string))

# upper case alphabet 65 - 90
# lower case alphabet 97 - 122
