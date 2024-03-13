from numpy import array, arange, pi, sin, cos, isreal
from numpy.linalg import eig, norm
import matplotlib.pyplot as plt


def arrow(p, v, c=(0, 0, 0), w=0.02):
    plt.quiver(p[0], p[1], v[0], v[1], units='xy', scale=1,
               color=c, width=w)


AA = [array([[1, -2], [2, 2]]),
      array([[3, 1], [1, 3]]),
      array([[2, 1], [0, 2]]),
      array([[2, 1], [0, 3]])]
T = arange(0, 2 * pi, pi / 500)
U = array([(cos(t), sin(t)) for t in T])
o = array([0, 0])
n = 140
plt.figure(figsize=(20, 5))
for A in AA:
    n += 1
    plt.subplot(n)
    V = array([A.dot(u) for u in U])
    plt.plot(U[:, 0], U[:, 1])
    plt.axis('scaled'), plt.xlim(-4, 4), plt.ylim(-4, 4)
    plt.plot(V[:, 0], V[:, 1])
    for u, v in zip(U[::20], V[::20]):
        arrow(u, v - u)
    Lmd, Vec = eig(A)
    if isreal(Lmd[0]):
        arrow(o, Lmd[0] * Vec[:, 0], c=(1, 0, 0), w=0.1)
    if isreal(Lmd[1]):
        arrow(o, Lmd[1] * Vec[:, 1], c=(0, 1, 0), w=0.1)
plt.show()
#plt.savefig('unitcircle2.png', bbox_inches='tight', pad_inches=0)
