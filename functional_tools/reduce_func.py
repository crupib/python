from functools import reduce

data = [1, 2, 3, 4, 5]

# Calculate the product of all elements
product = reduce(lambda x, y: x * y, data)

print(product)  # Output: 120
