import sys
import copy

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next
    def __str__(self):
        return str(self.cargo)
def print_list(node):
    while node:
        print node,
        node = node.next
    print    
def create(n, constructor=list):
    for _ in xrange(n):
        yield constructor()
        
Buffer_Header = [["deviceno",0],["blockno",0],["status",0],["data",0],["nhbuf",0],
		 ["phbuf",0],["nflbuf",0],["pflbuf",0]]

Hash_queue = ["blkno",0,"mod4"]
create(10,Hash_queue)
Device = []
DataArea = [1,2,3,4]
count = 0
while count < 40:
    Device.append(copy.deepcopy(Buffer_Header))
    count = count + 1

count = 0
while count < 40:
    Device[count][0][1] = count
    count = count + 1
    
count = 0
while count < 40:
    Device[count][1][1] = count
    count = count + 1
    
count = 0    
while count < 40:
    print Device[count]
    count = count + 1
Device[0][3][1] = DataArea
print Device[0][3][1][2]
buffer = []
buffer.append(Node(1))
buffer.append(Node(2))
buffer.append(Node(3))
buffer[0].next = buffer[1]
buffer[1].next = buffer[2]

buffer_header = buffer[0]
print_list(buffer_header)
