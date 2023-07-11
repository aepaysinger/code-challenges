def get_room_names():
    with open("./code_challenges/advent_of_code/room_name_input") as room_names_input:
        room_names = room_names_input.read().split("\n")
    return room_names

def get_incrypted_room_name():
    room_names = get_room_names()
    room_names = [room.split("-") for room in room_names]
    for room in room_names:
        letter_count = {}
        for i in range(len(room)-1):
            for character in room[i]:
                letter_count[character] = letter_count.get(character, 0) + 1
        print(letter_count)

    

    return room_names


# print(get_room_names())
print(get_incrypted_room_name())