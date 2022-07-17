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
    elif len(captains_room) >= 2:
        return "Don't forget the crew!" 
    else:
        return captains_room.pop()
        


if __name__ == "__main__":
    K = int(input())
    room_numbers = input().split(" ")
    print(find_the_captain(room_numbers))
