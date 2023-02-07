from operator import add, sub, mul


class ZipWith:
    def __init__(self, func):
        self.func = func

    def zip_it(self, array1, array2):
        return [self.func(a, b) for a, b in zip(array1, array2)]


def zip_with(func, array1, array2):
    zipping = ZipWith(func)

    return zipping.zip_it(array1, array2)


if __name__ == "__main__":
    func = add
    array1 = [10, 10, 10, 10]
    array2 = [0, 1, 2, 3]
    print(zip_with(func, array1, array2))
