from numpy import zeros, arange, random, linalg
import matplotlib.pyplot as plt

N, rho, sigma, tau = 100, 1.0, 0.1, 0.1
random.seed(2021)

x, y = zeros(N), zeros(N)
for i in range(N):
    x[i] = rho*x[i - 1] + sigma*random.normal(0, 1)
    y[i] = x[i] + tau*random.normal(0, 1)

A = zeros((N, 2 * N))
for i in range(N):
    for j in range(i + 1):
        A[i, j] = rho**(i - j) * sigma
    A[i, N + i] = tau
B = linalg.pinv(A)

v = B.dot(y)
z = zeros(N)
for i in range(N):
    z[i] = rho*z[i - 1] + sigma*v[i]
print(f'(y-x)^2 = {sum((y-x) ** 2)}')
print(f'(z-x)^2 = {sum((z-x) ** 2)}')

plt.figure(figsize=(20, 5))
T = arange(N)
plt.plot(T, x, color='black', linestyle = 'solid', label='real value')
plt.plot(T, y, color='black', linestyle = 'dotted', label='observed value')
plt.plot(T, z, color='black', linestyle = 'dashed', label='estimated value')
plt.legend()
plt.savefig('estimate2.png', bbox_inches='tight', pad_inches=0.05)
plt.show()

'''
(y-x)^2 = 0.9032093121921972
(z-x)^2 = 0.48559541437198783
'''
