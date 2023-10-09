# Write a function that takes a dictionary, string, and iterable of values.
# The dictionaries keys will be strings and the values will be functions.
# The return value should be the return value from the function from the input dict,  at the input string,
# when called with the values in the input iterable as arguments.
def find_the_function(functions, function_name, values):
    return functions[function_name](*values)


def adding(*nums):
    return sum(nums)


def even_it_up(*the_numbers):
    evens = []
    for number in the_numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens


if __name__ == "__main__":
    functions = {
        "adding": adding,
        "even_it_up": even_it_up,
    }
    function_name = "adding"
    the_numbers = [10, 13, 20]
    print(find_the_function(functions, function_name, the_numbers))
