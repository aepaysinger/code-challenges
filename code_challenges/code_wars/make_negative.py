def make_negative(number):
    if number < 0:
        return number
    else:
        return number * -1


if __name__ == "__main__":
    number = int(input())
    print(make_negative(number))
