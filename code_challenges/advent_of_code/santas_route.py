def get_directions():

    with open(
        "./code_challenges/advent_of_code/santas_directions"
    ) as elf_instructions:
        directions = elf_instructions.read()

    return directions


def follow_directions():
    directions = get_directions()
    x, y = 0, 0
    houses_visited = {(0, 0)}

   
    for direction in directions:
        if direction == "^":
            x += 1
            houses_visited.update((x, y))
        elif direction == "v":
            x -= 1
            houses_visited.update((x, y))
        elif houses_visited == "<":
            y += 1
            houses_visited.update((x, y))
        elif direction == ">":
            y -= 1
            houses_visited.update((x, y))
    
    return len(houses_visited)

# print(get_directions())
print(follow_directions())




