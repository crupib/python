import linklist
llist = linklist.SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.Atbegining("Sun")
#llist.AtEnd("Sat")
#llist.RemoveNode("Tue")
insertnode = llist.getNode("Wed",llist)
if insertnode == None:
  llist.AtEnd("Fri")
else:
  llist.Inbetween(insertnode,"Fri")
llist.LListprint()
