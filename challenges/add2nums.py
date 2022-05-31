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
        temp = l1.head
        temp2 = l2.head
        carry = 0
        rlist = LinkedList()
        node = Node(0) 
        while(temp):
          if carry == 1:
             node.data = (temp.data+temp2.data+1)
             carry = 0
          elif (temp.data+temp2.data) > 9:
            node.data = 0
            carry = 1
          else:
            node.data = (temp.data+temp2.data)
          node.next = nodenext
          temp = temp.next
          temp2 = temp2.next
        return rlist 
def main():
  l1 = [2,4,3]
  l2 = [5,6,4]
  llist1 = LinkedList()
  llist2 = LinkedList()
  sol = Solution()
  temp1=[]
  temp2=[]
  for x in reversed(l1):
      temp1.append(Node(x))
  for y in reversed(l2):
      temp2.append(Node(y))
  llist1.head = temp1[0]
  llist1.head.next=temp1[1]
  for item in temp1[2:len(temp1)]:
      llist1.head.next.next=item
#  llist1.printList()
  llist2.head = temp2[0]
  llist2.head.next=temp2[1]
  for item in temp2[2:len(temp2)]:
      llist2.head.next.next=item
#  llist2.printList()
  rlist=sol.addTwoNumbers(llist1,llist2)
if __name__ == "__main__":
    main()
