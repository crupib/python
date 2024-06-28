from numpy import array, linspace, identity, exp, pi, linalg, ones
from numpy.polynomial.legendre import Legendre
import matplotlib.pyplot as plt

with open('tablet.txt', 'r') as fd:
    data = eval(fd.read())
m = len(data)
t = linspace(0.0, 1.0, m)
x, y = zip(*[(z.real, z.imag) for z in data])

plt.figure(figsize=(7, 7))
plt.axis('scaled'), plt.xlim(-1, 1), plt.ylim(-1, 1)
plt.plot(x, y)
plt.scatter(x, y, s=16)
plt.show()
#plt.savefig('moji2d.png', bbox_inches='tight', pad_inches=0.05)
