import math
from string import ascii_letters

def mymax(list):
   tempmax = 0
   for i in list:
      if tempmax < i:
        tempmax = i
   return tempmax


def myodd(list):
    retlist=[]
    for i in list:
        if i%2 != 0:
          retlist.append(i)
    return retlist

# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverse(s) 
    if (s == rev): 
        return True
    return False
  
  
# Driver code 

allowed = set(ascii_letters)
s = "Madam In Eden, I'm Adam"
u = s.upper()
z = ''.join(l for l in u if l in allowed)
ans = isPalindrome(z) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 

mylist = [112,6,4,81,5,11,98,9,1,3,69,21,293]
print(mymax(mylist))
print(myodd(mylist))

