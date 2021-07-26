# selection sort algorithm
''' Selecton sort algorithm '''
def selection_sort(list1):
    ''' Selecton sort algorithm '''
    for fill_slot in range(len(list1) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list1[location] > list1[max_index]:
                max_index = location
        list1[fill_slot], list1[max_index] = list1[max_index], list1[fill_slot]
    return list1
def main():
    ''' Main '''
    list1 = [26,17,20,11,23,21,13,18,24,12,22,16,15,19,25]
    print("Starting state: ", list1)
    selection_sort(list1)
    print("Final state: ", list1)


if __name__ == "__main__":
    main()
