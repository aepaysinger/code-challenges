def get_room_names():
    with open("./code_challenges/advent_of_code/room_name_input") as room_names_input:
        room_names = room_names_input.read().split("\n")
    return room_names


def get_encrypted_room_name():
    room_names = [room.split("-") for room in get_room_names()]
    rooms = []

    for room in room_names:
        letter_count = {}
        for i in range(len(room) - 1):
            for character in room[i]:
                letter_count[character] = letter_count.get(character, 0) + 1
        start, end = room[-1].split("[")
        code = end[:-1]
        digits = int(start)
        rooms.append((digits, code, letter_count))

    total = 0
    real_rooms = []

    for i, (digits, code, letter_count) in enumerate(rooms):
        characters = []
        for letter in letter_count:
            if letter not in code:
                continue
            characters.append((letter, letter_count[letter]))
        characters = sorted(characters, key=by_letter)
        characters = sorted(characters, key=by_number, reverse=True)
        characters = "".join([character[0] for character in characters])
        if characters == code:
            total += digits
            real_rooms.append(room_names[i])

    return total, real_rooms


def translate_room_names(desired_room_name):
    _, real_rooms = get_encrypted_room_name()

    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    room_names = []

    for room in real_rooms:
        room_name = ""
        sector_id, _ = room[-1].split("[")
        sector_id = int(sector_id)
        for characters in room[:-1]:
            for i, character in enumerate(characters):
                index = alphabet.index(character)
                total = index + sector_id
                result = total % 26
                room_name += alphabet[result]
                if i == len(characters) - 1:
                    room_name += " "
        room_names.append(room_name[:-1])
        if room_name == desired_room_name:
            return sector_id

    return room_names


def by_number(character_and_amount):
    _, amount = character_and_amount
    return amount


def by_letter(character_and_amount):
    character, _ = character_and_amount
    return character
