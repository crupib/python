# A single node of a singly linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = val // 10, val % 10
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next
    def print_linked_list(self,item):
    # base case
      if item == None:
        return
    # lets print the current node 
      print(item.val)
    # print the next nodes
      self.print_linked_list(item.next)
    def linkedListToList(self,item,output):
    # base case
      if item == None:
        return
    # lets print the current node 
      output.append(item.val)
    # print the next nodes
      self.linkedListToList(item.next,output)
if __name__ == '__main__':
    a, a.next, a.next.next , a.next.next.next= ListNode(2), ListNode(4), ListNode(3), ListNode(9)
    b, b.next, b.next.next , b.next.next.next = ListNode(5), ListNode(6), ListNode(4), ListNode(2)
    result = Solution().addTwoNumbers(a, b)
    output = []
    Solution().print_linked_list(result)
    Solution().linkedListToList(result,output)  
    print(output)
