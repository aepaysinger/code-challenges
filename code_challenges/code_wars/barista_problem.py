def fastest_coffee_orders(orders):
    if orders == []:
        return 0
    cleaning_time = 0
    for i in range(1, len(orders)):
        cleaning_time = (2 * i) + cleaning_time
    time = 0
    orders.sort()
    for i in range(len(orders) + 1):
        time += sum(orders[:i])

    return time + cleaning_time


if __name__ == "__main__":
    orders = [2, 10, 5, 3, 9]
    print(fastest_coffee_orders(orders))
