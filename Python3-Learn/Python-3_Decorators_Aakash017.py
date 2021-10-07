def uppercase_decorator(function):
    def wrapper():
        fn = function()
        make_uppercase = fn.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    return "hello there!"


print(say_hi())
