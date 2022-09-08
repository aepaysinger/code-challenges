def parse(data):
    final_data = []
    number = 0
    for character in data:
        if character == "i":
            number += 1
        elif character == "d":
            number -= 1
        elif character == "s":
            number = number * number
        elif character == "o":
            final_data.append(number)

    return final_data


if __name__ == "__main__":
    data = "iiisdoso"
    print(parse(data))
