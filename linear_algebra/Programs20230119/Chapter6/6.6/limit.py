from numpy import array, sin, cos, pi, inf
from numpy.linalg import norm
import matplotlib.pyplot as plt


def A(t):
    return array([[cos(t), -sin(t)], [sin(t), cos(t)]])


x = array([1, 0])
P, L1, L2, Loo = [], [], [], []
M = range(1, 100)
for m in M:
    xm = A(pi / 2 / m).dot(x)
    P.append(xm)
    L1.append(norm(x - xm, ord=1))
    L2.append(norm(x - xm))
    Loo.append(norm(x - xm, ord=inf))

plt.figure(figsize=(10, 5))
plt.subplot(121)
for p in P:
    plt.plot(p[0], p[1], marker='.', color='black')
plt.subplot(122)
plt.xlim(0, 20)
plt.plot(M, L1), plt.text(1, L1[0], 'L1', fontsize=16)
plt.plot(M, L2), plt.text(1, L2[0], 'L2', fontsize=16)
plt.plot(M, Loo), plt.text(1, Loo[0], 'Loo', fontsize=16)
plt.show()
#plt.savefig('limit.png', bbox_inches='tight', pad_inches=0)
