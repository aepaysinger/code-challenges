def make_pairs(mixed_shoes):
    shoes = {}

    for foot, size in mixed_shoes:
        if size not in shoes:
            shoes[size] = {0: 0, 1: 0}
            shoes[size][foot] += 1
        else:
            shoes[size][foot] += 1

    return shoes


def find_pairs(mixed_shoes):
    shoes = make_pairs(mixed_shoes)
    shoe_pairs = False
    for size in shoes:
        if shoes[size][0] == shoes[size][1]:
            shoe_pairs = True
        else:
            return False
    return shoe_pairs


if __name__ == "__main__":
    mixed_shoes = [
        [0, 38],
        [0, 31],
        [1, 34],
        [0, 47],
        [0, 44],
        [1, 47],
        [1, 46],
        [0, 37],
        [0, 46],
        [1, 31],
        [1, 41],
        [1, 38],
        [0, 41],
        [0, 34],
    ]
    print(find_pairs(mixed_shoes))
