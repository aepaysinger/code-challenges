from operator import add, sub, mul


class ZipWith:
    def __init__(self, func, array1, array2):
        self.func = func
        self.array1 = array1
        self.array2 = array2

    def zip_with(self):
        return [self.func(a, b) for a, b in zip(self.array1, self.array2)]


def zip_with(func, array1, array2):
    zipping = ZipWith(func, array1, array2)

    return zipping.zip_with()


if __name__ == "__main__":
    func = add
    array1 = [10, 10, 10, 10]
    array2 = [0, 1, 2, 3]
    print(zip_with(func, array1, array2))
