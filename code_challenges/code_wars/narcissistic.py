def narcissistic(num):
    new_num = str(num)
    powered_num = []
    for number in new_num:
        number = int(number)
        powered_num.append(number**(len(new_num)))
    powered_num_total = 0
    for number in powered_num:
        powered_num_total += number
    if powered_num_total == num:
        return True
    else:
        return False
    


if __name__ == "__main__":
    num = 122
    print(narcissistic(num))
