from itertools import permutations


def find_mult_3(num):
    multiples = set()
    num = str(num)
    count = 0
    max_multiple = 0

    for i in range(len(num)):
        for perm in permutations(num, i + 1):
            multiple = int("".join(perm))
            if not multiple or multiple in multiples:
                continue
            multiples.add(multiple)
            if multiple % 3 == 0:
                max_multiple = max(max_multiple, multiple)
                count += 1

    return [count, max_multiple]
