from numpy import matrix, pi, sin, cos, linspace
from numpy.random import normal
from numpy.linalg import eig, eigh
import matplotlib.pylab as plt

N = 100
B = normal(0, 1, (N, N, 2))
A = matrix(B[:, :, 0] + 1j * B[:, :, 1])
Real = A + A.conj()
Hermite = A + A.H
PositiveSemiDefinite = A * A.H
PositiveComponents = abs(A)
Unitary = matrix(eigh(Hermite)[1])

X = A
#X = Real
#X = Hermite
#X = PositiveSemiDefinite
#X = PositiveComponents
#X = Unitary
Lmd = eig(X)[0]
r = max(abs(Lmd))
T = linspace(0, 2 * pi, 100)
plt.axis('equal')
plt.plot(r * cos(T), r * sin(T))
plt.scatter(Lmd.real, Lmd.imag, s=20)
plt.show()
#plt.savefig('A.png', bbox_inches='tight', pad_inches=0)
