def camp_cleanup_sections():

    with open(
        "/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/camp_cleanup_input"
    ) as sections:
        section_ids = sections.read().split("\n")

    return section_ids

print(camp_cleanup_sections())