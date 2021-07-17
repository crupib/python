''' interpolation search on ordered list '''
def BubbleSort(dataset):
    # start with the array length and decrement each time
    for i in range(len(dataset)-1, 0, -1):
        # examine each item pair
        for j in range(i):
            # swap items if needed
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
def IntPolsearch(list, x):
    idx0 = 0
    idxn = (len(list) - 1) 
    found = False
    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
      mid = idx0 + int(((float(idxn - idx0)/(list[idxn] - list[idx0])) * (x - list[idx0])))
      if list[mid] == x:
        found = True
        return found
      if list[mid] < x:
        idx0 = mid + 1
    return found
def main():
    list = [12,33, 11, 99, 22, 55, 90]
    sorted_list = BubbleSort(list)
    print(IntPolsearch(list,99))
    print(IntPolsearch(list,11))

if __name__ == "__main__":
    main()
