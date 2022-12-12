def rucksack_reorganization():
    supplies = open("/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/rucksack_input")
    items = supplies.read().split("\n")
    supplies.close()
    
    with open("/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/rucksack_input") as supplies:
        items = supplies.read().split("\n")

    return items

def find_common_character():
    items = rucksack_reorganization()
    first_half = []
    second_half = []
    # common_character = []
    for item in items:
        length = len(item)
        half_way = length // 2
        # first_half.append(item[0:half_way])
        # second_half.append(item[half_way:])
        first_half = item[0:half_way]
        second_half = item[half_way:]
        
    
    
    
    
    
        
    return common_character

# def find_priority():
#     priority_level = {
#         "a": 1,
#         "b": 2,
#         "c": 3,
#         "d": 4,
#         "e": 5,
#         "f": 6,
#         "g": 7,
#         "h": 8,
#         "i": 9,
#         "j": 10,
#         "k": 11,
#         "l": 12,
#         "m": 13,
#         "n": 14,
#         "o": 15,
#         "p": 16,
#         "q": 17,
#         "r": 18,
#         "s": 19,
#         "t": 20,
#         "u": 21,
#         "v": 22,
#         "w": 23,
#         "x": 24,
#         "y": 25,
#         "z": 26,
#         "A": 27,
#         "B": 28,
#         "C": 29,
#         "D": 30,
#         "E": 31,
#         "F": 32,
#         "G": 33,
#         "H": 34,
#         "I": 35,
#         "J": 36,
#         "K": 37,
#         "L": 38,
#         "M": 39,
#         "N": 40,
#         "O": 41,
#         "P": 42,
#         "Q": 43,
#         "R": 44,
#         "S": 45,
#         "T": 46,
#         "U": 47,
#         "V": 48,
#         "W": 49,
#         "X": 50,
#         "Y": 51,
#         "Z": 52,
#     }
#     common_characters = find_common_character()
#     priority_level_amount = 0
#     for character in common_characters:
#         priority_level_amount += priority_level[character]
#     return common_characters, priority_level_amount


print(find_common_character())