from itertools import permutations


def find_mult_3(num):
    multiples = set()
    multiples_of_3 = set()
    i = 1
    num = str(num)
    nums = [digit for digit in num]
    while i <= len(str(num)):
        perm = permutations(nums, i)
        for j in list(perm):
            multiples.add(j)
        i += 1

    for numbers in multiples:
        new_num = ""
        for number in numbers:
            new_num += number
        new_num = int(new_num)
        if new_num == 0:
            continue
        if new_num % 3 == 0:
            multiples_of_3.add(new_num)

    return [len(multiples_of_3), max(multiples_of_3)]
