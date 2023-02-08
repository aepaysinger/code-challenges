def make_pairs(mixed_shoes):
    shoes = {}
    for foot, size in mixed_shoes:
        shoes[size] = shoes.get(size, foot)
    print(shoes)


if __name__ == "__main__":
    mixed_shoes = [[0, 21], 
         [1, 23], 
         [1, 21], 
         [0, 23]]
    print(make_pairs(mixed_shoes))