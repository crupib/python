import matplotlib.pyplot as plt

with open('mypict1.txt', 'r') as fd:
    P = eval(fd.read())
x, y = zip(*P)
plt.scatter(x, y, s=30)
plt.axis('scaled'), plt.xlim(-0.25, 0.25), plt.ylim(-0.25, 0.25)
plt.show()
#plt.savefig('mypict2_2.png', bbox_inches='tight', pad_inches=0)
