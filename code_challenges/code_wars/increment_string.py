import re


def increment_string(characters):
    if characters == "":
        return "1"
    if characters[-1].isalpha():
        return characters + "1"

    parts = re.match(r"([a-zA-Z0-9]+[a-zA-Z])([0-9]+)", characters)

    first, second = parts.groups()

    characters = first

    numbers = int(second)
    numbers += 1
    numbers = str(numbers)
    numbers = numbers.zfill(len(second))
    numbers = str(numbers)
    characters += numbers

    return characters


if __name__ == "__main__":
    characters = "foobar99"
    print(increment_string(characters))
