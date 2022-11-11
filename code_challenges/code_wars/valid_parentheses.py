def valid_parentheses(characters):
    count = 0
    for character in characters:
        if character == "(":
            count += 1
        elif character == ")":
            count -= 1
        if count == -1:
            return False
    if count == 1:
        return False

    return True


if __name__ == "__main__":
    characters = ""
    print(valid_parentheses(characters))
