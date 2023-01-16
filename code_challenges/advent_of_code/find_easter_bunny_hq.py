def elves_directions():
    with open(
        "./code_challenges/advent_of_code/directions_to_easter_bunny_hq"
    ) as elf_directions:
        directions = elf_directions.read().split(",")
    return directions

print(elves_directions())