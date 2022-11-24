def unscrambled_eggs(code):
    decoded = code.replace("egg", "")

    return decoded


if __name__ == "__main__":
    code = "ceggodegge heggeregge"
    print(unscrambled_eggs(code))
