from numpy import linspace, cumsum, vdot, sort
from numpy.random import seed, uniform, normal
from gram_schmidt import gram_schmidt, proj
import matplotlib.pyplot as plt

n = 20
seed(2021)
x = sort(uniform(-1, 1, n))
z = 4 * x**3 - 3 * x
sigma = 0.2
y = z + normal(0, sigma, n)
E = gram_schmidt([x**0, x**1, x**2, x**3])
y0 = proj(z, E)

plt.figure(figsize=(15,5))
plt.errorbar(x, z, yerr=sigma, fmt='ro')
plt.plot(x, y, color='k', linestyle = 'solid')
plt.plot(x, y0, color='k', linestyle = 'dotted')
plt.show()
#plt.savefig('lstsqr.png', bbox_inches='tight', pad_inches=0)
