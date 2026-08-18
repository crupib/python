def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])

print(count([3,4,5,6,9,3]))