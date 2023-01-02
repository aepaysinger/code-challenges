def camp_cleanup_sections():

    with open(
        "./code_challenges/advent_of_code/camp_cleanup_input"
    ) as sections:
        section_ids = sections.read().split("\n")

    return section_ids


def get_sections():
    section_ids = camp_cleanup_sections()
    section_ids = [section_id.split(",") for section_id in section_ids]
    group_a = []
    group_b = []

    for section_id in section_ids:
        group_a.append(section_id[0])
        group_b.append(section_id[1])
    group_a = [group.split("-") for group in group_a]
    group_a = [(int(section[0]), int(section[1])) for section in group_a]
    group_b = [group.split("-") for group in group_b]
    group_b = [(int(section[0]), int(section[1])) for section in group_b]

    return group_a, group_b


def full_overlap():
    full_double_coverage = 0
    group_a, group_b = get_sections()
    for i, group in enumerate(group_a):
        if group[0] >= group_b[i][0] and group[1] <= group_b[i][1]:
            full_double_coverage += 1
        elif group_b[i][0] >= group[0] and group_b[i][1] <= group[1]:
            full_double_coverage += 1

    return full_double_coverage


def part_overlap():
    double_coverage = 0
    group_a, group_b = get_sections()

    for i, group in enumerate(group_a):
        if group_b[i][0] in range(group[0], group[1] + 1):
            double_coverage += 1
        elif group_b[i][1] in range(group[0], group[1] + 1):
            double_coverage += 1
        elif group[0] in range(group_b[i][0], group_b[i][1] + 1):
            double_coverage += 1
        elif group[1] in range(group_b[i][0], group_b[i][1] + 1):
            double_coverage += 1

    return double_coverage


print(camp_cleanup_sections())
print(full_overlap())
print(part_overlap())
