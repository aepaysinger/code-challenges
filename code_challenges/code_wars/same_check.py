def comp(arr1, arr2):
    if arr1 == [] or arr2 == []:
        return False
    for number in arr1:
        if (number * number) in arr2:
            arr2.remove(number * number)
        else:
            return False
    return True
