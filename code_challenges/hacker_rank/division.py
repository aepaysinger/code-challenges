from __future__ import division


def fun_division(a,b):
    print((a // b))
    print(round(a / b, 2))


if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    fun_division(a,b)