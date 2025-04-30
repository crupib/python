def bubbleSort(dataset):
    # start with the array length and decrement each time
    for i in range(len(dataset)-1, 0, -1):
        # examine each item pair
        for j in range(i):
            # swap items if needed
            if dataset[j][4] > dataset[j+1][4]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
