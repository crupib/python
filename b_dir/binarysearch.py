import random

def createRandomList(size):
    randomlist = []
    for i in range(0,size):
        n = random.randint(1,size)
        randomlist.append(n)
    return randomlist

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


L = createRandomList(500)
SL = selectionSort(L)
print(binary_search(SL,5))
