class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None
class SLinkedList:
   def __init__(self):
      self.head = None
   def Atbegining(self, data_in):
      NewNode = Node(data_in)
      NewNode.next = self.head
      self.head = NewNode
   def AtEnd(self, newdata):
      NewNode = Node(newdata)
      if self.head is None:
         self.head = NewNode
         return
      laste = self.head
      while(laste.next):
         laste = laste.next
      laste.next=NewNode
   def Inbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return
      NewNode = Node(newdata)
      NewNode.next = middle_node.next
      middle_node.next = NewNode

# Function to remove node
   def RemoveNode(self, Removekey):
      HeadVal = self.head
         
      if (HeadVal is not None):
         if (HeadVal.data == Removekey):
            self.head = HeadVal.next
            HeadVal = None
            return
      while (HeadVal is not None):
         if HeadVal.data == Removekey:
            break
         prev = HeadVal
         HeadVal = HeadVal.next

      if (HeadVal == None):
         return

      prev.next = HeadVal.next
      HeadVal = None

   def getNode(self,nodeval,list):
      insertnode = self.head
      while(insertnode):
        if insertnode.data == nodeval :
           return insertnode
        insertnode = insertnode.next
      list.AtEnd("Sat")
      return None
   def LListprint(self):
      printval = self.head
      while (printval):
         print(printval.data),
         printval = printval.next

llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.Atbegining("Sun")
llist.AtEnd("Sat")
llist.RemoveNode("Tue")
insertnode = llist.getNode("",llist)
llist.Inbetween(insertnode,"Fri")
llist.LListprint()
