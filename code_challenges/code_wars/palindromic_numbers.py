def palindromize(number):
    count = 0
    morphed_number = str(number)
    while True:
        reverse_morph = morphed_number[::-1]
        if morphed_number == reverse_morph:
            return str(count) + " " + morphed_number
        morphed_number = str(int(reverse_morph) + int(morphed_number))
        count += 1
