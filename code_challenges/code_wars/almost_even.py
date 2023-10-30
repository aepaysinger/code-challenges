def split_integer(num, parts):
    part = num // parts
    integer_parts = [part for _ in range(parts)]
    i = len(integer_parts) - 1
    for _ in range(num % parts):
        integer_parts[i] += 1
        i -= 1
    return integer_parts
