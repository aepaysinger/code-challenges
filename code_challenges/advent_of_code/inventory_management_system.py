def get_box_ids():
    with open('code_challenges/advent_of_code/box_ids_input') as box_ids_input:
        box_ids = box_ids_input.read().split("\n")
    return box_ids


def find_box_ids_checksum():
    box_ids = get_box_ids()
    id_counts = {}
    twos_count = 0
    threes_count = 0
    for box in box_ids:
        id_counts[box] = {}
        counts = set()
        for letter in box:
            id_counts[box][letter] = id_counts[box].get(letter, 0) + 1
        for count in id_counts[box].values():
            counts.add(count)
        if 2 in counts and 3 in counts:
            twos_count += 1
            threes_count += 1
        elif 2 in counts:
            twos_count += 1
        elif 3 in counts:
            threes_count += 1
    return id_counts
    
    # return twos_count * threes_count   


def find_similar_box():
    box_ids_counts = find_box_ids_checksum()
    box_ids_counts = [[box, box_ids_counts[box]] for box in box_ids_counts]
    # print(box_ids_counts)
    
    for i, (box, count) in enumerate(box_ids_counts[:-2]):
        for (other_box, other_count) in box_ids_counts[i + 1:]:
            is_similar, letters = compare_boxes(count, other_count)
            if is_similar:
                return letters
         
    

def compare_boxes(box_count, other_box_count):
    #return boolean, and wrong letters

# for each enumerate(box)
#     for each other get_box_ids
#         compare each to other 


# print(get_box_ids())
# print(find_box_ids_checksum())
print(find_similar_box())