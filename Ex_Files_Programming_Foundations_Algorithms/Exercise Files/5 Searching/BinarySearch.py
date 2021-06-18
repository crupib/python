''' Binary search on ordered list '''
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
def BinarySearch(list, item):
    first = 0
    last = len(list)-1
    found = False
    while first <= last and not found:
      midpoint = (first + last)//2
      if list[midpoint] == item:
        found = True
      else:
        if item < list[midpoint]:
           last = midpoint - 1
        else:
           first = midpoint + 1
    return found
def main():
    list = [12,33, 11, 99, 22, 55, 90]
    sorted_list = BubbleSort(list)
    print(BinarySearch(list,12))
    print(BinarySearch(list,91))

if __name__ == "__main__":
    main()


