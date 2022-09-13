def snail(trail):

    final_path = []
    stop = 0
    for path in trail:
        stop += len(path)
    while True:
        if len(final_path) == stop:
            break
        final_path.extend(trail[0])
        trail.remove(trail[0])
        if len(final_path) == stop:
            break
        for path in trail:
            final_path.append(path[-1])
            del path[-1]
        if len(final_path) == stop:
            break
        final_path.extend((trail[-1][::-1]))
        trail.remove(trail[-1])
        if len(final_path) == stop:
            break
        for path in reversed(trail):
            final_path.append(path[0])
            del path[0]

    return final_path


if __name__ == "__main__":
    trail = [
        [1, 2, 3], 
        [8, 9, 4], 
        [7, 6, 5],
    ]

    print(snail(trail))
