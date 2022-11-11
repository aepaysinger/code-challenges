def coffee_wait(orders, machines):
    if orders == []:
        return 0
    cleaning_time = 0
    if machines == 1:
        for i in range(1,len(orders)):
            cleaning_time = (2 * i) + cleaning_time 
        time = 0
        orders.sort()
        for i in range(len(orders)+1):
            time += sum(orders[:i])
        return time + cleaning_time
    else:
        new_orders = mutiple_machines(orders, machines)
        print(new_orders)

def mutiple_machines(orders, machines):
    machine_orders = {}
    for i in range(machines):
        machine_orders[i+1] = []
    orders.sort()
    if machines == 2:
        for i in range(len(orders)):
            if len(orders) == 2:
                machine_orders[1] = orders[i]
                machine_orders[2] = orders[i+1]
            else:
                machine_orders[1] = orders[i], orders[i+1]
                machine_orders[2] = orders[i+2]
                for i in range(len(orders)):
                    while i+4 < len(orders):
                        machine_orders[1] = orders[i+3]
                        machine_orders[2] = orders[i+4]
    print(machine_orders)

            
            

    
    return machine_orders
    
    

if __name__ == "__main__":
    orders = [2,10,5,3,9] #2 3 5 9 10
    machines = 2
    print(coffee_wait(orders, machines))