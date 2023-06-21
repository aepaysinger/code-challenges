def get_smoke_input():
    with open("code_challenges/advent_of_code/smoke_input") as smoke_input:
        smoke_levels = smoke_input.read().split("\n")
    return smoke_levels

def find_lowest_point():
    smoke_levels = get_smoke_input()
    # print(smoke_levels)
    # smoke_levels = [row.split() for row in smoke_levels]
    
    lowest_points = []
    for i, level in enumerate(smoke_levels):
        behind = i - 1
        before = i + 1
        above = smoke_levels[i - 1][i]
        under = smoke_levels[i + 1][i]
        if i == 0:
            print(level)

        
    
                
    
    
    
    # for row in smoke_levels:
    #     print(",".join(row))
    # print(smoke_levels)

# print(get_smoke_input())
print(find_lowest_point())
# 0['2199943210', 
# 1 '3987894921', 
# 2 '9856789892', 
# 3 '8767896789', 
# 4 '9899965678']