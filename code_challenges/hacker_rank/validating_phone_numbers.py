def check_for_mobile_number(list_of_numbers):
    result = ""
    for number in list_of_numbers:
        if len(number) == 10 and number.isdigit():
            if number[0] == "7" or number[0] == "8" or number[0] == "9":
                result += "YES\n"
            else:
                result += "NO\n"
        else:
            result += "NO\n"
    return result.rstrip()


if __name__ == "__main__":
    amount = int(input())
    numbers_list = []
    for number in range(amount):
        numbers_list.append(input())
    print(check_for_mobile_number(numbers_list))
