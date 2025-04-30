def addition(x,y):
    return x + y
from functools import reduce
input_list = [1, 2, 3, 4, 5]
# Without Lambda function
print(reduce(addition, input_list))
# With Lambda function
print(reduce(lambda x,y: x+y, input_list))
# Output: 15
