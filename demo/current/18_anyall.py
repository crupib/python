list1 = [True, True, True]

print("Output of any(): ", any(list1))  # Output: True
print("Output of all(): ", all(list1))  # Output: True

list2 = [False, True, True]
print("Output of any(): ", any(list2))  # Output: True
print("Output of all(): ", all(list2))  # Output: False
mydict1 = {"user": "admin", "age": "23", "password": 123,  "lastname": "" }

print(any(mydict1.values()))   # Output: True
print(all(mydict1.values()))   # Output: True

mydict2 = {"user": "admin", "age": "25", "password": ""}
print(any(mydict2.values()))   # Output: True

# Output will be "False", because value of the  "password" field is empty. 
print(all(mydict2.values()))   # Output: False 
