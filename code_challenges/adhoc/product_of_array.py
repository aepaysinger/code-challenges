import math

def product_of_array(array):
    # product_array = []
    # count = 0
    # for _ in range(len(array)):
    #     product = 1
    #     for i in range(len(array)):
    #         if i != count:
    #             product *= array[i]
    #     count += 1
    #     product_array.append(product)
    # return product_array
    product_of_array = []
    
    for i in range(len(array)):
        # need_to_add = array.pop(0)
        # product_of_array.append(math.prod(array))
        # array.append(need_to_add)
        if i == 0:
            product_of_array.append(math.prod(array[1:]))
        else:
        
            product_of_array.append(math.prod(array[:i] + array[i+1:]))
        
    return product_of_array



if __name__ == "__main__":
    array = [1,2,3,4]
    print(product_of_array(array))