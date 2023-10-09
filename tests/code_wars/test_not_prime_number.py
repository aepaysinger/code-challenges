from code_challenges.code_wars.not_prime_number import (
    not_primes,
    is_prime,
    in_single_primes,
)


def test_not_primes():
    actual = not_primes(2, 222)
    expected = [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75, 77]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_is_prime_true():
    actual = is_prime(23)
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_is_prime_false():
    actual = is_prime(22)
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_in_single_primes_true():
    actual = in_single_primes(57)
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_in_sinlge_primes_false():
    actual = in_single_primes(38)
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"
