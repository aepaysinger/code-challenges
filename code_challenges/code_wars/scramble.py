def scramble(scrambled_characters, unscrambled_characters):
    scrambled_counter, unscrambled_counter = count_characters(
        scrambled_characters, unscrambled_characters
    )
    for character in unscrambled_counter:
        if (
            character not in scrambled_counter
            or unscrambled_counter[character] > scrambled_counter[character]
        ):
            return False

    return True


def count_characters(scrambled_characters, unscrambled_characters):
    scrambled_characters_amount = {}
    unscrambled_characters_amount = {}
    for character in scrambled_characters:
        if character in scrambled_characters_amount:
            scrambled_characters_amount[character] += 1
        else:
            scrambled_characters_amount[character] = 1
    for character in unscrambled_characters:
        if character in unscrambled_characters_amount:
            unscrambled_characters_amount[character] += 1
        else:
            unscrambled_characters_amount[character] = 1
    print(scrambled_characters_amount, unscrambled_characters_amount)
    return scrambled_characters_amount, unscrambled_characters_amount


if __name__ == "__main__":
    scrambled_characters = "rkqodlw"
    unscrambled_characters = "world"
    print(scramble(scrambled_characters, unscrambled_characters))
