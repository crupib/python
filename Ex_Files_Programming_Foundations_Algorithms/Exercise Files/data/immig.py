import shellsort
#import mybubsort

def LinearSearch(list, item):
  index = 0
  found = []
  while index < len(list):
    if list[index][4] == item:
      found.append(list[index])
      index = index + 1
    else:
      index = index + 1
  return found

found = []
ifile=open("hist.txt", "r")
lines=ifile.readlines()
data=[tuple(line.strip().split()) for line in lines]
shellsort.shellSort(data)
print("******************************************************")
for item in data:
   print(item) 
j=LinearSearch(data,"2000-09-19")
print("******************************************************")
for item in j:
   print(item)
