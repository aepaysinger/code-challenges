import math


def find_smallest(prices):
    smallest_amount, smallest_amount_day = math.inf, None
    
    for i, price in enumerate(prices):
        if price < smallest_amount:
            smallest_amount = price
            smallest_amount_day = i
    if smallest_amount == prices[-1]:
        prices = prices[:-1]

    
    return smallest_amount, smallest_amount_day

def buy_sell_stock(prices):
    smallest_amount, smallest_amount_day = find_smallest(prices)
    largest_amount, largest_amount_day = 0, None
    
    if smallest_amount == prices[-1]:
        prices = prices[:-1]
        smallest_amount, smallest_amount_day = find_smallest(prices)
    
        
    for i, price in enumerate(prices[smallest_amount_day + 1:]):
        if price > largest_amount:
            largest_amount = price
            largest_amount_day = i
    
    if largest_amount_day is None:
        return 0
        
    return largest_amount - smallest_amount


if __name__ == "__main__":
    prices = [7, 5, 6]
    print(buy_sell_stock(prices))