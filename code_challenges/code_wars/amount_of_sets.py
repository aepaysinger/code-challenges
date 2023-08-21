from itertools import combinations


def find_amount_of_sets(characters):
    sets_of_characters = set()
    characters = set(characters)
    for i in range(len(characters) + 1):
        sets_of_characters.update(set(combinations(characters, i)))
    return len(sets_of_characters) - 1


if __name__ == "__main__":
    characters = [1, 2, 3, 4, 1]
    print(find_amount_of_sets(characters))
