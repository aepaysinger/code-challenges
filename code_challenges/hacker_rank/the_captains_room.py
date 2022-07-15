def find_the_captain(room_numbers):
    # family_room = []
    # captains_room = []
    # for room_number in room_numbers:
    #     if room_number in family_room:
    #         family_room.append(room_number)
    #     elif room_number not in captains_room:
    #         captains_room.append(room_number)
    #     elif room_number in captains_room:
    #         captains_room.remove(room_number)
    #         family_room.append(room_number)
    # if captains_room == []:
    #     return "where did the captain go?"
    # else:
    #     return int(('').join(captains_room))   
    # family_room = []
    for room_number in room_numbers:
        captains_room = [room_number for room_numbers in captains_room if captains_room.count(room_number) >= 2]   
    return captains_room


if __name__ == '__main__':
    # K = int(input())
    # print(K)
    room_numbers = '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2'.split(' ')
    print(find_the_captain(room_numbers))