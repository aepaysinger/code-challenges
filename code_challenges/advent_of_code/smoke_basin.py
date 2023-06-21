def get_smoke_input():
    with open("code_challenges/advent_of_code/smoke_input") as smoke_input:
        smoke_levels = smoke_input.read().split("\n")
    return smoke_levels

def find_lowest_point():
    smoke_levels = get_smoke_input()
    # print(smoke_levels)
    # smoke_levels = [row.split() for row in smoke_levels]
    # smoke_levels = [[','.join(number)]for row in smoke_levels for number in row]
    # smoke_levels = []
    print(smoke_levels)
    # res = [int(test_str[idx : idx + K]) for idx in range(0, len(test_str), K)]
    # lowest_points = []
    # for i, level in enumerate(smoke_levels):
    #     if i >= 1 and i <= 3:
    #         behind = i - 1
    #         after = i + 1
    #         above = smoke_levels[i - 1][i]
    #         under = smoke_levels[i + 1][i]
    #         for i, number in enumerate(level):
    #             number = int(number)
    #             if i == 0:
    #                 if number < level[above] and number < level[after] and number < level[under]:
    #                     lowest_points.append(number)
    #             elif i == len(level) - 1:
    #                 if number < level[above] and number < level[behind] and number < level[under]:
    #                     lowest_points.append(number)
    #             else:
    #                 if number < level[behind] and number < level[after] and number < level[above] and number < level[under]:
    #                     lowest_points.append(number)
    # print(lowest_points)
                
                

        
    
                
    
    
    
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