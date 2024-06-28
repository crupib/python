from numpy import matrix
from numpy.linalg import eig, norm
from numpy.random import normal, seed
import matplotlib.pyplot as plt

def gelfand(m, s):
    seed(s)
    A = matrix(normal(0, 1, (m, m)))
    lmd = max(abs(eig(A)[0]))
    X = range(1, 50)
    P = [A**n for n in range(50)]
    Y = [norm(P[n], 2)**(1 / n) for n in X]
    plt.plot([X[0], X[-1]], [lmd, lmd], c='k')
    for i in range(m):
        for j in range(m):
            plt.plot(X, [abs(P[n][i, j])**(1 / n) for n in X])
    plt.plot(X, Y, c='k')
    plt.text(max(X), max(Y), f'seed={s}',
             size=18, ha='right', va='top')

plt.figure(figsize=(20, 8))
n = 241
for s in [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]:
    plt.subplot(n)
    gelfand(3, s)
    n += 1

plt.show()    
#plt.savefig('gelfand.png', bbox_inches='tight', pad_inches=0)

