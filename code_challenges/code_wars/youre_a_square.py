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
    