from functools import partial

# Original function
def multiply(x, y):
    return x * y
# Create a new function that multiplies by 2

double = partial(multiply, y=2)
result = double(5)

print(result)  # Output: 10
