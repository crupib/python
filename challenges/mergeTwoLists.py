import string
from algorithms.sort import merge_sort
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def print_linked_list(self,item):
    # base case
      if item == None:
        return
    # lets print the current node 
      print(item.val)
    # print the next nodes
      self.print_linked_list(item.next)
    def listToLinkedList(self, list):
      last=None
      for item in list:
          current=ListNode(item)
          current.val = item
          current.next = last
          last=current
      return current
    def mergeTwoLists(swlf,headA, headB):
  
    # A dummy node to store the result
     dummyNode = ListNode(0)
     
     # Tail stores the last node
     tail = dummyNode
     while True:
     
          # If any of the list gets completely empty
          # directly join all the elements of the other list
          if headA is None:
               tail.next = headB
               break
          if headB is None:
               tail.next = headA
               break
     
          # Compare the data of the lists and whichever is smaller is
          # appended to the last of the merged list and the head is changed
          if headA.val <= headB.val:
               tail.next = headA
               headA = headA.next
          else:
               tail.next = headB
               headB = headB.next
     
          # Advance the tail
          tail = tail.next
     
     # Returns the head of the merged list
     return dummyNode.next
     
def main():
  list1 = [1,2,4] 
  list2 = [1,3,4]

  assert  len(list1) >= 0 and len(list1) <= 50, "Failed out of range"
  assert  len(list2) >= 0 and len(list2) <= 50, "Failed out of range"
  for i in list1:
       assert  i >= -100 and i <= 100, "list1 has a value out of range"
  for i in list2:
       assert  i >= -100 and i <= 100, "list2 has a value  out of range"
  sol = Solution()
  list1.reverse()
  list2.reverse()
  llist1 =Solution().listToLinkedList(list1) 
  llist2 =Solution().listToLinkedList(list2)
  
  #sol.print_linked_list(llist1)
  #sol.print_linked_list(llist2)
  retmergedlists = sol.mergeTwoLists(llist1, llist2)
  sol.print_linked_list(retmergedlists)
if __name__ == "__main__":
    main()
