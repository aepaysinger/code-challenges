def create_phone_number(numbers):
    str_numbers = ""
    for number in numbers:
        str_numbers += str(number)
    if len(str_numbers) > 10:
        return f"({str_numbers[0:3]}) {str_numbers[3:6]}-{str_numbers[6:10]} (these were extra {str_numbers[10:]})"
    elif len(str_numbers) < 10:
        return "You don't have enought numbers"
    else:
        return f"({str_numbers[0:3]}) {str_numbers[3:6]}-{str_numbers[6:10]}"


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(create_phone_number(numbers))
