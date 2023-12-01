def get_even(mylist):
    return [num for num in mylist if num%2 == 0] 

mylist = [1,2,3,4,5,6,7,8]

print("Even numbers are:", get_even(mylist))
