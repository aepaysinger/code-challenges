from math import sqrt


def not_primes(a, b):
    numbers = []
    for num in range(a, b):
        if num < 22:
            continue
        if not in_single_primes(num):
            continue
        if is_prime(num):
            continue
        else:
            numbers.append(num)

    return numbers


def is_prime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def in_single_primes(num):
    single_primes = {"2", "3", "5", "7"}
    for digit in str(num):
        if digit in single_primes:
            continue
        else:
            return False
    return True
