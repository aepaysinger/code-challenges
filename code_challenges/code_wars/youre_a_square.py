import math


def is_square(n):    
    if n < 0:
        return False
    x = math.sqrt(n)
    if x == int(x):
        return True
    else:
        return False


if __name__ == "__main__":
    n = 34
    print(is_square(n))
    

    # fun things