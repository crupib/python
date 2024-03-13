from numpy import array, pi, sin, cos
import matplotlib.pyplot as plt

t = pi / 4
A = array([[cos(t), -sin(t)], [sin(t), cos(t)]])

with open('mypict1.txt', 'r') as fd:
    P = eval(fd.read())

Q = [A.dot(p) for p in P]
x, y = zip(*Q)
plt.scatter(x, y, s=1)
plt.axis('equal'), plt.show()
#plt.savefig('mypict5.png', bbox_inches='tight', pad_inches=0)
