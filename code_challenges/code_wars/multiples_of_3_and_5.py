def multiples_of_3_and_5(n):
    multiples = []
    total = 0
    for number in range(1, n):
        if number % 3 == 0 or number % 5 == 0:
            multiples.append(number)
    for number in multiples:
        total += number
    return total


if __name__ == "__main__":
    n = int(input())
    print(multiples_of_3_and_5(n))
