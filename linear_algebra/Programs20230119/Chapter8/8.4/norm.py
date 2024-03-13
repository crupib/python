from numpy import matrix
from numpy.linalg import eig, norm
from numpy.random import normal, seed
import matplotlib.pyplot as plt

def power(m, s):
    seed(s)
    A = matrix(normal(0, 2, (m, m)))
    lmd = max(abs(eig(A)[0])) + 0.1
    X = range(50)
    P = [(A / lmd)**n for n in X]
    Y = [norm(B, 2) for B in P]
    plt.plot([X[0], X[-1]], [0, 0], c='k')
    for i in range(m):
        for j in range(m):
            plt.plot(X, [abs(B[i, j]) for B in P])
    plt.plot(X, Y, c='k')
    plt.text(max(X), max(Y), f'seed={s}',
             size=18, ha='right', va='top')


plt.figure(figsize=(20, 8))
n = 241
for s in [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]:
    plt.subplot(n)
    power(3, s)
    n += 1

plt.show()  
#plt.savefig('norm.pdf', bbox_inches='tight', pad_inches=0)

