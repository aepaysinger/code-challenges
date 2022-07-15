def find_the_captain(room_numbers):
    family_room = set()
    captains_room = set()
    for room_number in room_numbers:
        if room_number in family_room:
            continue
        elif room_number not in captains_room:
            captains_room.add(room_number)
        elif room_number in captains_room:
            captains_room.remove(room_number)
            family_room.add(room_number)
    if not captains_room:
        return "where did the captain go?"
    else:
        return captains_room.pop()


if __name__ == "__main__":
    # K = int(input())
    # print(K)
    room_numbers = (
        "1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2".split(" ")
    )
    print(find_the_captain(room_numbers))
