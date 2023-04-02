def product_of_array(array):
    forward = [1] * len(array)
    backwards = [1] * len(array)
    product_of_array = [1] * len(array)

    for i in range(1, len(array)):
        forward[i] = forward[i - 1] * array[i - 1]
    
    for i in range(len(array) - 2, -1, -1):
        backwards[i] = backwards[i + 1] * array[i + 1]

    for i in range(len(product_of_array)):
        product_of_array[i] = forward[i] * backwards[i]

    return product_of_array



if __name__ == "__main__":
    array = [1,2,3,4]
    print(product_of_array(array)) [24, 12, 8, 6]