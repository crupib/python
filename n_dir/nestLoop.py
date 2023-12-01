list1 = [1,2,3]
list2 = ['a', 'b']

result = [(x, y) for x in list1 for y in list2]

for x,y in result: print(x, y)
