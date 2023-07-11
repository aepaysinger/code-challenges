def count_skills(tree, required):
    if required == set():
        return 0

    visited_levels = set()
    for number in required:
        level = tree[number]
        while level not in visited_levels and level not in required:
            visited_levels.add(level)
            level = tree[level]

    return len(visited_levels) + len(required)
