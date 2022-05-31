# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data, end=""),
      current = current.next
    print("\n")

class Solution(object):
  def addTwoNumbers(self, l1, l2):
        temp1 = l1.head
        temp2 = l2.head
        sum = 0
        carry = 0
        rlist = LinkedList()
        while(temp1):
          sum = temp1.data+temp2.data
          if carry == 1:
            sum = sum+1
          if sum >= 10:
             carry = 1
             sum = sum - 10
             rlist.insert(sum) 
          else:
             carry = 0
             rlist.insert(sum)
          temp1 = temp1.next
          temp2 = temp2.next
        if carry == 1:
           rlist.insert(sum+1)
        return rlist

# Singly Linked List with insertion and print methods
def main():
#  l1 = [9,9,9,9,9,9,9]
#  l2 = [9,9,9,9]
#  l1 = [2,4,3]
#  l2 = [5,6,4]
  l1 = [0]
  l2 = [0]
  llist1 = LinkedList()
  llist2 = LinkedList()
  sol = Solution()
  temp1=[]
  temp2=[]

  for x in reversed(l1):
      temp1.append(Node(x))
  for y in reversed(l2):
      temp2.append(Node(y))
  
  numzeros = len(l1)-len(l2)
  for item in temp1:
     llist1.insert(item.data) 
  for item in temp2:
     llist2.insert(item.data) 
  if numzeros > 0:
     for i in range(numzeros):
         llist2.insert(0)   
  rlist=sol.addTwoNumbers(llist1,llist2)
  rlist.printLL()
if __name__ == "__main__":
    main()
