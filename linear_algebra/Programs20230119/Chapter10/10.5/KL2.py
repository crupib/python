import numpy as np
import matplotlib.pyplot as plt

tmax, N = 100, 1000
dt = tmax / N

np.random.seed(2021)
W = np.random.normal(0, dt, (2, N))
Noise = np.random.normal(0, 0.25, (4, N))
B = W.cumsum(axis=1)
P = np.array([[1, 2], [1, -2], [2, 1], [-2, 1]])
A0 = P.dot(B)
A = A0 + Noise
U, S, V = np.linalg.svd(A)
print(f'singular values = {S}')

C = U[:, :2].dot(np.diag(S[:2]).dot(V[:2, :]))
plt.figure(figsize=(20, 5))
T = np.linspace(0, tmax, N)
plt.subplot(131)
for i in range(4):
    plt.plot(T, A[i], label=f'A[{i}]')
    plt.legend()
plt.subplot(132)
for i in range(2):
    plt.plot(T, V[i], label=f'V[{i}]')
    plt.legend()
plt.subplot(133)
for i in range(4):
    plt.plot(T, C[i], label=f'C[{i}]')
    plt.legend()
error0 = np.sum((A0 - A)**2, axis=1) / N
error1 = np.sum((A0 - C)**2, axis=1) / N
print(f'error0 = {error0}')
print(f'error1 = {error1}')
plt.savefig('KL2.png', bbox_inches='tight', pad_inches=0.05)
plt.show()
