def split_integer(num, parts):
    integer_parts = []
    part = num // parts
    for _ in range(parts):
        integer_parts.append(part)
    i = len(integer_parts) - 1
    for _ in range((num % parts)):
        integer_parts[i] += 1
        i -= 1
    return integer_parts
