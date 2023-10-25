def get_smoke_input():
    with open("code_challenges/advent_of_code/smoke_input") as smoke_input:
        smoke_levels = smoke_input.read().split("\n")
    return smoke_levels

def transform_smoke_levels():
    smoke_levels_input = get_smoke_input()
    smoke_levels_input = [','.join(row) for row in smoke_levels_input]
    smoke_levels =[]
    for row in smoke_levels_input:
        holding = []
        for number in row:
            if number.isdigit():
                holding.append(int(number))
        smoke_levels.append(holding)
    return smoke_levels

def find_lowest_point():
    smoke_levels = transform_smoke_levels()
   
    lowest_points = []
    for row, level in enumerate(smoke_levels):
        if row == 0:
            for i, number in enumerate(level):
                behind = i - 1
                after = i + 1
                under = smoke_levels[row + 1][i]
                if i == 0:
                    if number < level[after] and number < level[under]:
                        lowest_points.append(number)
                elif i == len(level) - 1:
                    if number < level[behind] and number < level[under]:
                        lowest_points.append(number)
                else:
                    if number < level[behind] and number < level[after] and number < under:
                        lowest_points.append(number)
        elif row >= 1 and row <= len(smoke_levels) - 2:
            for i, number in enumerate(level):
                behind = i - 1
                after = i + 1
                above = smoke_levels[row - 1][i]
                under = smoke_levels[row + 1][i]
                if i == 0:
                    if number < above and number < level[after] and number < under:
                        lowest_points.append(number)
                elif i == len(level) - 1:
                    if number < above and number < level[behind] and number < under:
                        lowest_points.append(number)
                else:
                    if number < level[behind] and number < level[after] and number < above and number < under:
                        lowest_points.append(number)
        elif row == len(smoke_levels) - 1:
            for i, number in enumerate(level):
                behind = i - 1
                after = i + 1
                above = smoke_levels[row - 1][i]
                if i == 0:
                    if number < above and number < level[after]:
                        lowest_points.append(number)
                elif i == len(level) - 1:
                    if number < level[behind] and number < above:
                        lowest_points.append(number)
                else:
                    if number < level[behind] and number < level[after] and number < above:
                        lowest_points.append(number)

    return sum(lowest_points) + len(lowest_points)

print(find_lowest_point())
#535 too high