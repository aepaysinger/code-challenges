def palindromize(number):
    count = 0
    morphed_number = str(number)
    while True:
        front_half = morphed_number[: len(morphed_number) // 2]
        if len(morphed_number) % 2 == 0:
            second_half = morphed_number[len(morphed_number) // 2 :]
        else:
            second_half = morphed_number[len(morphed_number) // 2 + 1 :]
        if second_half == front_half[::-1]:
            return str(count) + " " + morphed_number
        reverse_morph = morphed_number[::-1]
        morphed_number = int(reverse_morph) + int(morphed_number)
        morphed_number = str(morphed_number)
        count += 1
