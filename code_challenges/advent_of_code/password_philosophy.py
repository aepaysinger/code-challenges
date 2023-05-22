def get_password_input():
    with open("./code_challenges/advent_of_code/password_input") as password_inputs:
        passwords_to_check = password_inputs.read().split("\n")

    return [password.split(" ") for password in passwords_to_check]


def break_up_password_input():
    passwords_to_check = get_password_input()
    password_ranges = []
    letters_to_check = []
    passwords = []

    for password_range, letter_to_check, password in passwords_to_check:
        password_ranges.append(password_range.split("-"))
        letters_to_check.append(letter_to_check[0])
        passwords.append(password)

    return password_ranges, letters_to_check, passwords


def check_password_validity_a():
    password_ranges, letters_to_check, passwords = break_up_password_input()

    valid_passwords = 0

    for i in range(len(password_ranges)):
        count = 0
        for letter in passwords[i]:
            if letter == letters_to_check[i]:
                count += 1
        if count >= int(password_ranges[i][0]) and count <= int(password_ranges[i][1]):
            valid_passwords += 1

    return valid_passwords


def check_password_validity_b():
    password_indexes_to_check, letters_to_check, passwords = break_up_password_input()
    valid_passwords = 0
    password_indexes_to_check = [
        [int(index[0]) - 1, int(index[1]) - 1] for index in password_indexes_to_check
    ]

    for i, index in enumerate(password_indexes_to_check):
        if (
            letters_to_check[i] == passwords[i][index[0]]
            or letters_to_check[i] == passwords[i][index[1]]
        ):
            valid_passwords += 1

    return valid_passwords


print(get_password_input())
# print(break_up_password_input())
# print(check_password_validity_a())
# print(check_password_validity_b())
# 782 is too high
