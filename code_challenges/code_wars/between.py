def between(num1, num2):
    if num1 > num2:
        return "incorrect range, enter the smaller number first"
    final = []
    for number in range(num1, (num2 + 1)):
        final.append(number)
    return final


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(between(a, b))
