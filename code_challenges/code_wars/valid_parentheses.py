def valid_parentheses(characters):
    # open = 0
    # close = 0
    count = 0
    for character in characters:
        if character == "(":
            # open += 1
            count += 1
        elif character == ")":
            # close += 1
            count -= 1
        if count == -1:
            return False
    if count == 1:
        return False
    # if open == close:
    #     return True
    # else:
    #     return False
    return True


if __name__ == "__main__":
    characters = ""
    print(valid_parentheses(characters))
