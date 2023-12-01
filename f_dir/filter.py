def less_than_10(x):
    if x < 10:
        return x 
input_list = [2, 3, 4, 5, 10, 12, 14] 
# Without lambda
print("Original List      ", input_list)
print("Without lambda < 10",list(filter(less_than_10, input_list)))
# using lambda function 
print("With lambda < 10   ",list(filter(lambda x: x < 10, input_list)))
# Output: [2, 3, 4, 5]
