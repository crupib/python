# Definition for singly-linked list.
# Node class
class Node:

# Function to initialize the node object
   def __init__(self, data):
     self.data = data # Assign data
     self.next = None # Initialize
# Linked List class
# A simple Python program to introduce a linked list
# Linked List class contains a Node object
class LinkedList:
# Function to initialize head
   def __init__(self):
     self.head = None
   def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
def main():
  l1 = [2,4,3]
  l2 = [5,6,4]
  llist1 = LinkedList()
  llist2 = LinkedList()
  temp1=[]
  temp2=[]
  for x in reversed(l1):
      temp1.append(Node(x))
  for y in reversed(l2):
      temp2.append(Node(y))
  for i in temp1:
     print(i.data)
  for i in temp2:
     print(i.data)
  llist1.head = temp1[0]
  llist1.head.next=temp1[1]
if __name__ == "__main__":
    main()
