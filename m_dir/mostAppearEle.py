mylist = [1,5,8,6,5,9,6,9,5,6,9,6,5,4,"a","a","b","b","a","a","a"]

print(max(set(mylist), key=mylist.count))
