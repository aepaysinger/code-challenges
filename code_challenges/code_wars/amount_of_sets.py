import math


def find_amount_of_sets(characters):
    characters = set(characters)
    total_list = [1]
    total = 1
    if len(characters) == 0:
        return 0
    for i in range(1, len(characters)):
        total += total
        total_list.append(total)

    return sum(total_list)
