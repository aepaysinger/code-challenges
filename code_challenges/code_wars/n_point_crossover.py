def crossover(ns, xs, ys):
    sections = sorted(set(ns))
    xs_list = xs.copy()
    ys_list = ys.copy()

    if len(sections) == 0:
        return xs, ys
    elif len(sections) == 1:
        for number in range(sections[0], len(xs)):
            xs_list[number] = ys[number]
            ys_list[number] = xs[number]
    elif len(sections) == 2:
        for number in range(sections[0], sections[1]):
            xs_list[number] = ys[number]
            ys_list[number] = xs[number]
    else:
        for number in range(sections[0], sections[1]):
            xs_list[number] = ys[number]
            ys_list[number] = xs[number]
        for number in range(sections[2], len(xs)):
            xs_list[number] = ys[number]
            ys_list[number] = xs[number]

    return xs_list, ys_list
