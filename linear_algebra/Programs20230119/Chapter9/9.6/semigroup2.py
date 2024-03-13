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


fig, axs = plt.subplots(1, 3, figsize=(20, 5))
for x in range(3):
    s, n = sum(S[x]), len(S[x])
    print(s / tmax)
    m = s / n
    axs[x].hist(S[x], bins=10)
    t = arange(0, 3, 0.01)
    axs[x].plot(t, exp(-t / m) / m * s)
    axs[x].set_xlim(0, 3), axs[x].set_ylim(0, 600)

plt.show()
#plt.savefig('semigroup2.png', bbox_inches='tight', pad_inches=0.05)

