def get_map():
    with open("./code_challenges/advent_of_code/map_input") as tree_plots:
        map = tree_plots.read().split("\n")

    return map


def trees_encountered():
    map = get_map()
    # map = [row + row for row in map]
    stop = len(map) - 1
    trees = 0
    steps = 3
    
    for i, path in enumerate(map):
        if i == stop:
            break
        if steps > len(path) - 1:
        #     map = [row + row for row in map]
        #     print(map)
            while steps > len(path) - 1:
                path += path
        if map[i+1][steps] == "#":
            trees += 1
        steps += 3
            
        
    return trees    

# print(get_map())
print(trees_encountered())