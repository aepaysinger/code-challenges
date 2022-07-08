def count_up(n):
    result = ""
    for number in range(n):
        result = result + str(number + 1)
    return result


if __name__ == '__main__':
    n = int(input())
    print(count_up(n))