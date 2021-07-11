import mybubsort

def LinearSearch(list, item):
  index = 0
  found = False
  while index < len(list) and  found is False:
    if list[index][4] == item:
      found = True
    else:
      index = index + 1
  return found


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
mybubsort.bubbleSort(data)
while i < len(data):
  print(data[i])
  i = i + 1
print(LinearSearch(data,"2000-09-19"))
