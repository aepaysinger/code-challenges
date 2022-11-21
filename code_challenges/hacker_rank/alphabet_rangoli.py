def alphabet_rangoli(rangoli_size):
    design = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    # amount_of_dashes = int(rangoli_size + (rangoli_size -1)) - 1 #4
    # amount_of_letters = int(rangoli_size + (rangoli_size - 1)) #5
    # rangoli_length = amount_of_dashes + amount_of_letters #9
    # pattern = []
    # count = amount_of_letters
    # for _ in range(rangoli_size):
    #     pattern.append("-"*count + design[rangoli_size-1] + "-"*count )
    #     count -= 2
    # return "\n".join(pattern)
#the length of rangoli is ((size - 1) * 4) + 1
#the amount of rows is double the size - 1
    pattern = [design[(rangoli_size - 1)]]
    previouse_pattern = []
    for i in range(rangoli_size):

        pattern.append(design[(rangoli_size - 1) - i])
    print(pattern)

    


if __name__ == "__main__":
    rangoli_size = 3
    print(alphabet_rangoli(rangoli_size))


 #size + (size -1) - 1 = dashes, 18
 # size + size - 1 = letters, 19
 # dashes + letters = len
    #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----