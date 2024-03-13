from numpy import array, linspace, sqrt, random, linalg
import matplotlib.pyplot as plt

n, m = 30, 1000
random.seed(2021)
x = linspace(0.0, 1.0, m)
w = random.normal(0.0, sqrt(1.0/m), m)
y = w.cumsum()
tA = array([x**j for j in range(n + 1)])
A = tA.T
S = linalg.solve(tA.dot(A), tA.dot(y))
L = linalg.lstsq(A, y, rcond=None)[0]

fig, axs = plt.subplots(1, 2, figsize=(15, 5))
for ax, B, title in zip(axs, [S, L], ['solve', 'lstsq']):
    z = B.dot(tA)
    ax.plot(x, y), ax.plot(x, z), ax.set_ylim(-0.7, 1)
    ax.text(0, -0.6, f'linslg.{title}', fontsize=16)
plt.show()
#plt.savefig('lstsqr.png', bbox_inches='tight', pad_inches=0.05)
