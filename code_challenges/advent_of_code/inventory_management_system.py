def get_box_ids():
    with open("code_challenges/advent_of_code/box_ids_input") as box_ids_input:
        box_ids = box_ids_input.read().split("\n")
    return box_ids


def find_box_ids_checksum():
    box_ids = get_box_ids()
    id_counts = get_id_counts()
    twos_count = 0
    threes_count = 0
    for box in box_ids:
        counts = set()
        for count in id_counts[box].values():
            counts.add(count)
        if 2 in counts and 3 in counts:
            twos_count += 1
            threes_count += 1
        if 2 in counts:
            twos_count += 1
        if 3 in counts:
            threes_count += 1
    return twos_count * threes_count


def get_id_counts():
    box_ids = get_box_ids()
    id_counts = {}
    for box in box_ids:
        id_counts[box] = {}
        counts = set()
        for letter in box:
            id_counts[box][letter] = id_counts[box].get(letter, 0) + 1
    return id_counts


def find_similar_box():
    box_ids_counts = get_id_counts()
    box_ids_counts = [[box, box_ids_counts[box]] for box in box_ids_counts]

    for i, (box, box_count) in enumerate(box_ids_counts[:-2]):
        for other_box, other_count in box_ids_counts[i + 1 :]:
            is_similar, letters = compare_boxes(box_count, other_count)
            if is_similar:
                similar_letters = [letter for letter in box if letter not in letters]
                return "".join(similar_letters)


def compare_boxes(box_count, other_box_count):
    wrong_letters = []

    for letter in box_count:
        if letter in other_box_count:
            if box_count[letter] != other_box_count[letter]:
                amount = box_count[letter] - other_box_count[letter]
                if amount < 0:
                    amount *= -1
                wrong_letters.append(letter * amount)
        else:
            wrong_letters.append(letter * box_count[letter])
    for letter in other_box_count:
        if letter in box_count:
            if box_count[letter] != other_box_count[letter]:
                amount = box_count[letter] - other_box_count[letter]
                if amount < 0:
                    amount *= -1
                wrong_letters.append(letter * amount)
        else:
            wrong_letters.append(letter * other_box_count[letter])

    return len(wrong_letters) == 2, wrong_letters
