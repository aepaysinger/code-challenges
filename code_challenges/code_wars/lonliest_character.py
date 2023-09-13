def loneliest(strng):
    characters_space_count = {}
    strng = strng.strip()
    count = 0
    old_count = 0
    current_character = strng[0]

    for i in range(1, len(strng)):
        if strng[i] == " ":
            count += 1
        else:
            characters_space_count[current_character] = count + old_count
            old_count = count
            count = 0
            current_character = strng[i]
    characters_space_count[current_character] = count + old_count

    return [
        character
        for character, count in characters_space_count.items()
        if count == max(characters_space_count.values())
    ]
