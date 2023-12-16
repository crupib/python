from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This is the wrapper function."""
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def my_function():
    """This is my function."""
    pass

print(my_function.__name__)  # Output: 'my_function'
print(my_function.__doc__)   # Output: 'This is my function.'
