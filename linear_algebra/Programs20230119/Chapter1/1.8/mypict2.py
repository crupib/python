import matplotlib.pyplot as plt

with open('mypict1.txt', 'r') as fd:
    P = eval(fd.read())
x, y = zip(*P)
plt.scatter(x, y, s=3)
plt.axis('scaled'), plt.xlim(-1, 1), plt.ylim(-1, 1)
plt.show()
#plt.savefig('mypict2.png', bbox_inches='tight', pad_inches=0)
