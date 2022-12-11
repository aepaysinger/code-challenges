def rucksack_reorganization():
    supplies = open("/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/rucksack_input")
    items = supplies.read().split("\n")
    supplies.close()
    
    with open("/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/rucksack_input") as supplies:
        items = supplies.read().split("\n")

def find_common_character(items):
    common_characters = []
    for item in items:
        length = len(item)
        half_way = length // 2
        part_1 = item[0:half_way]
        part_2 = item[half_way:]
        for character in part_1:
            if character in part_2:
                common_characters.append(character)

    return common_characters

def find_priority():
    common_characters = find_common_character()
    print(common_characters)


    # return 

print(rucksack_reorganization())
# print(find_common_character())