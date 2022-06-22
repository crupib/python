# A single node of a singly linked list
class ListNode:
  # constructor
  def __init__(self, val = None, next=None): 
    self.val = val
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
    self.val = 0
    self.next = None
  # insertion method for the linked list
  def insert(self,val):
    newNode = ListNode(val)
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
      print(current.val),
      current = current.next
class Solution(object):
    def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret

# Singly Linked List with insertion and print methods
def main():
  l1 = [2,4,3]
  l2 = [5,6,4]
  llist1 = LinkedList()
  llist2 = LinkedList()
  sol = Solution()
  temp1=[]
  temp2=[]

  for x in reversed(l1):
      temp1.append(ListNode(x))
  for y in reversed(l2):
      temp2.append(ListNode(y))
  numzeros = len(l1)-len(l2)
  for item in temp1:
     llist1.insert(item.val) 
  for item in temp2:
     llist2.insert(item.val) 
  if numzeros > 0:
     for i in range(numzeros):
         llist2.insert(0)   
  rlist=sol.addTwoNumbers(llist1,llist2)
  rlist.printLL()
if __name__ == "__main__":
    main()
