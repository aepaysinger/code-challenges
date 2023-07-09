def expanded_form(num):
    num = str(num)
    expanded = ""
    i = 1
    for character in num:
        if character == "0":
            i += 1
            continue
        zeroes = len(num) - i
        expanded += character + (zeroes * "0") + " + "
        i += 1
    return expanded[:-3]
