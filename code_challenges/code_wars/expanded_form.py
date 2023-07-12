def expanded_form(num):
    num = str(num)
    expanded = ""

    for i, character in enumerate(num, start=1):
        if character == "0":
            continue
        zeroes = len(num) - i
        expanded += character + (zeroes * "0") + " + "
    return expanded[:-3]
