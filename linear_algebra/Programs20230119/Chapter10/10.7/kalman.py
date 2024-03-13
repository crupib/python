from numpy import *
import matplotlib.pyplot as plt

random.seed(2021)
N, r, s, t = 100, 1.0, 0.1, 0.1
T = range(N)

x, y, z = zeros(N), zeros(N), zeros(N)
a = s**2
for i in range(N):
    x[i] = r * x[i - 1] + s * random.normal(0, 1)
    y[i] = x[i] + t * random.normal(0, 1)
    z[i] = r * z[i - 1] + a / (t**2 + a) * (y[i] - r * z[i - 1])
    c = a - a**2 / (t**2 + a)
    a = r * c + s**2
print(f'(y-x)^2 = {sum((y-x)**2)}')
print(f'(z-x)^2 = {sum((z-x)**2)}')

plt.figure(figsize=(20, 5))
plt.plot(T, x, color='black', linestyle = 'solid', label='real value')
plt.plot(T, y, color='black', linestyle = 'dotted', label='observed value')
plt.plot(T, z, color='black', linestyle = 'dashed',label='estimated value')
plt.legend()
plt.savefig('kalman.png', bbox_inches='tight', pad_inches=0.05)
plt.show()

'''
(y-x)^2 = 0.9032093121921977
(z-x)^2 = 0.6551470144698649
'''
