from itertools import combinations


def chances_of_finding_the_letter_a(the_letters, number_of_indices):
    the_combinations = list(combinations(the_letters, number_of_indices))
    combinations_with_a = []
    for pairs in the_combinations:
        if "a" in pairs:
            combinations_with_a.append(pairs)
        else:
            pass
    total_length = len(the_combinations)
    length_with_a = len(combinations_with_a)

    return round((length_with_a / total_length), 4)


if __name__ == "__main__":
    length_of_list = int(input())
    the_letters = input().split()
    number_of_indices = int(input)
    print(chances_of_finding_the_letter_a(the_letters, number_of_indices))
