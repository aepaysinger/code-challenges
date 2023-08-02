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
    similar_boxes = []
    
    
    for i, box in enumerate(box_ids_counts):
        count = i
        not_same = 0
        if i == len(box_ids_counts) - 1:
            break
        for letter in box[0]:
            print(count, box, letter)
            boxes_to_check = []
            # if letter in box_ids_counts[count]:
            #     boxes_to_check.append(box_ids_counts[count])
            if letter not in box_ids_counts[count + 1][0]:
                not_same += 1
            if not_same == 2:
                letter = box[0][0]
                print(box[0][0])
                not_same = 0
                count = i
                break
        
        if not_same == 1:
            similar_boxes.append((box)[0])            
    
    return similar_boxes




# print(get_box_ids())
# print(find_box_ids_checksum())
print(find_similar_box())