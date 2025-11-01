""" This is a nest function with a decorator. It uses for hiding the inside function or it can be used by not changing the
original function. """

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

# MY example of using the decorator
@log_decorator
def multiply(a, b):
    return a * b

add(3, 5)
multiply(4, 6)
