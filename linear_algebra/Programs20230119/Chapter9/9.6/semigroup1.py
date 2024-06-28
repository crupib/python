from numpy import arange, array, eye, exp
from numpy.random import choice, seed
from numpy.linalg import eig
import matplotlib.pyplot as plt

seed(2020)
dt, tmax = 0.01, 1000
T = arange(0.0, tmax, dt)
G = array([[-3,  4,  0], [ 1, -4,  5], [ 2,  0, -5]])
v = eig(G)[1][:, 0]
print(v / sum(v))
dP = eye(3) + G * dt

X = [0]
S = [[dt], [], []]
for t in T:
    x = X[-1]
    y = choice(3, p=dP[:, x])
    if x == y:
        S[x][-1] += dt
    else:
        S[y].append(dt)
    X.append(y)


plt.figure(figsize=(15, 5))

plt.plot(T[:2000], X[:2000])
plt.yticks(range(3))
plt.show()
#plt.savefig('semigroup1.png', bbox_inches='tight', pad_inches=0.05)
