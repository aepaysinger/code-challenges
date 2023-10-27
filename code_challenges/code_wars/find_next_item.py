def cycle(direction, values, value):
    for i in range(len(values)):
        if values[i] == value:
            if i == len(values) - 1 and direction > 0:
                return values[0]
            if i == 0 and direction < 0:
                return values[-1]

            return values[i + direction]
    return None
