from itertools import combinations


def making_combinations(a_string, a_number):
    list_a = list(combinations(a_string, a_number))
    print(list_a.sort)

making_combinations('HACK', 2)
