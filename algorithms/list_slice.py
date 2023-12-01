"""lists and slices"""
# declare list
MYLIST = [1, 2, 3, 4, 5, "Hello"]
#print list
print(MYLIST)
print(MYLIST[2])
print(MYLIST[-1])
MYLIST2 = MYLIST[1:5]
print(MYLIST2)
MYLIST[1] = 20
print(MYLIST)
MYLIST.append("How are you doosh")
print(MYLIST)
del MYLIST[5]
print(MYLIST)
