def compressing_strings(a_string):
    count = 0
    current_letter = a_string[0]
    compressed_string = ""

    for letter in a_string:
        if letter == current_letter:
            count += 1
        else:
            compressed_string += f"({count}, {current_letter}) "
            current_letter = letter
            count = 1
    return f"{compressed_string}({count}, {current_letter})"


if __name__ == "__main__":
    a_string = str(input())
    print(compressing_strings(a_string))
