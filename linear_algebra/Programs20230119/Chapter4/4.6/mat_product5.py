from numpy.random import normal
from numpy.linalg import inv
import matplotlib.pyplot as plt
from time import time

N = range(100, 2100, 100)
T = [[], [], []]

for n in N:
    t0 = time()
    A = normal(0, 1, (n, n))
    t1 = time()
    A.dot(A)
    t2 = time()
    inv(A)
    t3 = time()
    print(n, end=', ')
    t = (t0, t1, t2, t3)
    for i in range(3):
        T[i].append(t[i + 1] - t[i])

label = ['f(x)', 'g(x)', 'h(x)']
for i in range(3):
    plt.plot(N, T[i])
    plt.text(N[-1], T[i][-1], label[i],  fontsize=18)
#plt.show()
plt.savefig('mat_product5.png', bbox_inches='tight', pad_inches=0)
