def fastest_coffee_orders(orders):
    if orders == []:
        return 0
    cleaning_time = 0
    for i in range(1,len(orders)):
        cleaning_time = (2 * i) + cleaning_time 
    time = 0
    orders.sort()
    for order in orders:
        # print(orders[:i], sum(orders[:i]), time)
        # order = sum(orders[:i])
        # print(order, time)
        time += order + time 
        print(time)
    print(cleaning_time)
    
    return time + cleaning_time
   
    

if __name__ == "__main__":
    orders = [4,3,2]
    print(fastest_coffee_orders(orders))
# 2 = 2
#2 2 + 3 = 7 --- 9
#2 2 + 3 + 5 = 12 --- 21
#2 2 + 3 + 5 + 9 = 21 ---- 42
#2 2 + 3 + 5 + 9 + 10 = 31------ 73
# 
# total 73 (missing 2 in the wait time)