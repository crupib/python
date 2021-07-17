# try out the Python queue functions
from collections import deque

# create a new empty deque object that will function as a queue
queue = deque()

# add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
<<<<<<< HEAD
=======
queue.append(5)
>>>>>>> bf1f356919b573a7da1241281434e8ce81c67d27

# print the queue contents
print(queue)

# pop an item off the front of the queue
x = queue.popleft()
print(x)
<<<<<<< HEAD
=======
x = queue.popleft()
print(x)
>>>>>>> bf1f356919b573a7da1241281434e8ce81c67d27
print(queue)
