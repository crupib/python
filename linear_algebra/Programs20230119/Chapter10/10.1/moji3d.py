from numpy import array, linspace, identity, exp, pi, linalg, ones
from numpy.polynomial.legendre import Legendre
import matplotlib.pyplot as plt

with open('tablet.txt', 'r') as fd:
    data = eval(fd.read())
m = len(data)
t = linspace(0.0, 1.0, m)
x, y = zip(*[(z.real, z.imag) for z in data])

plt.figure(figsize=(7, 7))
ax = plt.subplot(111, projection='3d')
ax.set_xlim(0, 1), ax.set_ylim(-1, 1), ax.set_zlim(-1, 1)
ax.plot(t, x, y)
ax.scatter(t, x, y, s=16)
plt.show()
#plt.savefig('moji3d.png', bbox_inches='tight', pad_inches=0.05)
