def increment_string(characters):
    if characters == "":
        return "1"
    if characters[-1].isalpha():
        return characters + "1"
    
    numbers = ""
    stop = None
    for i in range(len(characters) - 1, -1, -1):
        if characters[i].isdigit():
            numbers += characters[i]
            stop = i
        else:
            break

    characters = characters[:stop]
    numbers = numbers[::-1]
    length = len(numbers)
    numbers = int(numbers)
    numbers += 1
    numbers = str(numbers)
    numbers = numbers.zfill(length)
    numbers = str(numbers)
    characters += numbers

    return characters


if __name__ == "__main__":
    characters = "fo99obar99"
    print(increment_string(characters))
