


def get_room_names():
    with open("./code_challenges/advent_of_code/room_name_input") as room_names_input:
        room_names = room_names_input.read().split("\n")
    return room_names

def get_incrypted_room_name():
    room_names = get_room_names()
    room_names = [room.split("-") for room in room_names]
    rooms = {}
    for room in room_names:
        letter_count = {}
        for i in range(len(room)-1):
            for character in room[i]:
                letter_count[character] = letter_count.get(character, 0) + 1
        rooms[room[-1]] = letter_count
    # for room in rooms:
    #     room = room.split("[")
        # print(room[1][:-1])
    total = 0
    for room, room_code in rooms.items():
        room_code = {val[0] : val[1] for val in sorted(room_code.items(), key = lambda x: (-x[1], x[0]))}
        i = 0
        print(room_code)
        # for character in room_code:
        #     print(character, room_code)
            # if character == "[":
            #     total += int(room.split('[')[0])
            # elif character == room.split('[')[1][i]:
            #     i += 1
            # else:
            #     print(character)
            #     continue
    # print(rooms)
    
        # for character in room.split("[")[1][:-1]:
        
        # room = room.split("[")
        # print(room, room_code)
        
    # res = {val[0] : val[1] for val in sorted(test_dict.items(), key = lambda x: (-x[1], x[0]))}

    
    
    # return rooms


# print(get_room_names())
print(get_incrypted_room_name())