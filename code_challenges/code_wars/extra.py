def coffee_wait(orders):
    if orders == []:
        return 0
    cleaning_time = 0
    
    for i in range(1,len(orders)):
        cleaning_time = (2 * i) + cleaning_time 
    time = 0
    orders.sort()
    for i in range(len(orders)+1):
        time += sum(orders[:i])
    return time + cleaning_time

if __name__ == "__main__":
    orders = [9,10]
    print(coffee_wait(orders))

# 2 3 5 7 == 46       2 3 9 == 27
# 4 6 == 16           5 10 == 22
# ----- 62            ------ 49

# 2 3 4 == 22         2 3 5 == 23
# 5 6 7 == 40         9 10 == 
# 62