def hello_goodbye(func):

    def inner():
        print("Hello Hello")
        func()
        print("Goodbye Goodbye!")

    return inner

@hello_goodbye
def hello():
    print("Hello Wolrd!")

hello()


# def hello():
#     print("Hello Wolrd!")

# def hello_goodbye(func):

#     def inner():
#         print("Hello Hello")
#         func()
#         print("Goodbye Goodbye!")

#     return inner

# decorated_func = display_info(hello)
# decorated_func()