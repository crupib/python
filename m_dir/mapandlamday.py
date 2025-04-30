def square(x):
    return x*x

input_list = [2, 3, 4, 5, 6]
# Without lambda 
result = map(square, input_list)
print("map run   ", list(result))
# Using lambda function 
result = map(lambda x: x*x, input_list)
# converting the numbers into a list
print("lambda run", list(result))
# Output: [4, 9, 16, 25, 36]
