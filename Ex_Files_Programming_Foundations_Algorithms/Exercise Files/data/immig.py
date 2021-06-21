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

ifile=open("hist.txt", "r")
lines=ifile.readlines()
data=[tuple(line.strip().split()) for line in lines]
print("*************************************************************************")
print()
i = 0
while i < len(data):
  print(data[i])
  i = i + 1
i = 0
print("*************************************************************************")
print()
bubbleSort(data)
while i < len(data):
  print(data[i])
  i = i + 1
