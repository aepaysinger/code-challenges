def weird_or_not_weird(n):
    if n % 2 != 0:
        return "Weird"
    elif n % 2 == 0 and n > 20:
        return "Not Weird"
    elif n % 2 == 0 and n in range(2, 6):
        return "Not Weird"
    elif n % 2 == 0 and n in range(6, 21):
        return "Weird"


if __name__ == "__main__":
    n = int(input().strip())
    print(weird_or_not_weird(n))
