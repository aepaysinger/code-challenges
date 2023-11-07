import re


def increment_string(characters):
    if characters == "":
        return "1"
    if characters[-1].isalpha():
        return characters + "1"

    parts = re.match(r"([a-zA-Z0-9]+[a-zA-Z])([0-9]+)", characters)

    first_half_characters, nums_at_end = parts.groups()

    numbers = int(nums_at_end)
    numbers += 1
    numbers = str(numbers)
    numbers = numbers.zfill(len(nums_at_end))

    return first_half_characters + numbers


if __name__ == "__main__":
    characters = "foobar99"
    print(increment_string(characters))
