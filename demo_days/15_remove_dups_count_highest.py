#!/usr/bin/python3
numbers = [1,1,1,2,2,3,4,5,6,7,7,8,9,9,9]
print(list(set(numbers)))
new_list = ['a','b','a','d','e','g','g','a','c','f','k','t','u','z','x','a']
print("Most frequent element:", max(set(new_list),key= new_list.count))
