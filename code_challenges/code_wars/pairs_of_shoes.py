from collections import Counter


def make_pairs(mixed_shoes):
    shoes = {}
    
    for foot, size in mixed_shoes:
        if size not in shoes:
            shoes[size] = {0: 0, 1: 0}
            shoes[size][foot] += 1
        else:
            shoes[size][foot] +=1

    return shoes

def find_pairs(mixed_shoes):
    shoes = make_pairs(mixed_shoes)
    shoe_pairs = False
    for size in shoes:
        if shoes[size][0] == shoes[size][1]:
            shoe_pairs = True
    return shoe_pairs


if __name__ == "__main__":
    mixed_shoes = [[0, 23], [1, 23], [1, 23], [0, 21], [0, 23], [0, 23]]
    print(find_pairs(mixed_shoes))

    # use a counter --> collections counter