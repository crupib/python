from numpy import array, arange, exp, sin, cos
from numpy.random import uniform
import matplotlib.pylab as plt


def B1(lmd1, lmd2):
    return lambda t: array([[exp(lmd1 * t), 0],
                            [0, exp(lmd2 * t)]])


def B2(lmd):
    return lambda t: exp(lmd * t) * array([[1, 0], [t, 1]])


def B3(a, b):
    return lambda t: exp(a * t) * array([
        [ cos(b * t), sin(b * t)],
        [-sin(b * t), cos(b * t)]])

# B1(lmd1, lmd2), B2(lmd), B3(a, b)
#
#fig = plt.figure(figsize=(20, 5))
#pos = 140
#for B in [B1(1, 0), B1(1, 1), B1(1, 2), B1(1, -1)]:
#
#fig = plt.figure(figsize=(10, 5))
#pos = 120
#for B in [B2(0), B2(1)]:
#
#fig = plt.figure(figsize=(10, 5))
#pos = 120
#for B in [B3(0, 1), B3(1, 1)]:
B = B3(1, 1)
if True:
    #pos += 1
    V = uniform(-1, 1, (100, 2))
    T = arange(-10, 10, 0.01)
    #plt.subplot(pos)
    plt.axis('scaled'), plt.xlim(-1, 1), plt.ylim(-1, 1)
    [plt.plot(*zip(*[B(t).dot(v) for t in T])) for v in V]

#plt.show()
plt.savefig('3-2.pdf', bbox_inches='tight', pad_inches=0.00)
