def bubble_tea_calculator(tea_base, add_ons, loyalty_discount):
    tea_base_options = {
        "milk": 4.35,
        "oolong": 4.60,
        "rose": 5.85,
        "mango": 5.47,
    }
    add_on_options = {
        "boba": .50,
        "lychee": .75,
        "jelly": .65,
        "taro": 1.00,
        "chia": .35,
    }
    customer_total = tea_base_options[tea_base]
    for add_on in add_ons:
        customer_total += add_on_options[add_on]

    if loyalty_discount:
        customer_total -= 1.00
    
    return f"The cost is ${customer_total:.2f}"
    




if __name__ == "__main__":
    tea_base = "milk"
    add_ons = ["boba", "jelly", "taro"]
    loyalty_discount = False
    print(bubble_tea_calculator(tea_base, add_ons, loyalty_discount))