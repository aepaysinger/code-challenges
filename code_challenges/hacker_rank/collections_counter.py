from collections import Counter


def rhagu_shoe_orders(shoe_sizes, shoe_order_and_size):
    inventory = Counter(shoe_sizes)
    money_made = 0
    for size, price in shoe_order_and_size:
        if inventory[size] > 0:
            money_made += int(price)
            inventory.subtract([size])
    print(money_made)


if __name__ == "__main__":
    number_of_shoes = int("10")
    shoe_sizes = "2 3 4 5 6 8 7 6 5 18".split()
    number_of_customers = int("6")
    shoe_order_and_size = []
    customers = ["6 55", "6 45", "6 55", "4 40", "18 60", "10 50"]
    for i in range(number_of_customers):
        shoe_order_and_size.append(customers[i].split())
    rhagu_shoe_orders(shoe_sizes, shoe_order_and_size)
    print(input())
