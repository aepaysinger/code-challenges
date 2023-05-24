def turns_on_road(x, y):
    turns = 0
    if x > 1:
        turns += (x - 1) * 4
    if y > 1:
        turns += ((y-1) * 4) + 1
    if y == 1:
        turns += 1
    if x < 1:
        turns += ((x * -1) * 4) - 1  
    if y < 1:
        turns += ((y * -1) * 4) - 1
    return 
x = 1
y = -1