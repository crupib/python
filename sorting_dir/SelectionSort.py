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

L = createRandomList(50)
print(selectionSort(L))
    
