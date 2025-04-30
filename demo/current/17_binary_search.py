import bisect
import timeit  
def binary_search_bisect(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1
  
  
# Test array
arr = [2, 3, 4, 10, 40, 45, 56, 57, 69, 70, 81, 99, 100]
x = 99
  
# Function call
start = timeit.default_timer()
result = binary_search_bisect(arr, x)
print(timeit.default_timer() - start)
  
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
