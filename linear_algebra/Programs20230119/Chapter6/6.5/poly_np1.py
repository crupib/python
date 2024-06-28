from numpy import array, linspace, sqrt, ones, pi
import matplotlib.pyplot as plt
from gram_schmidt import gram_schmidt

m = 10000
D = linspace(-1, 1, m + 1)
x = array([(D[n] + D[n+1])/2 for n in range(m)])

inner = {
    'Legendre': lambda f, g: f.dot(g) * 2/m,
    'Chebyshev1': lambda f, g: f.dot(g/sqrt(1 - x**2)) * 2/m,
    'Chebyshev2': lambda f, g: f.dot(g*sqrt(1 - x**2)) * 2/m,
}

A = [x**n for n in range(6)]
E = gram_schmidt(A, inner=inner['Legendre'])
for e in E:
    plt.plot(x, e)
plt.show()
#plt.savefig('Legendre_np1.png', bbox_inches='tight', pad_inches=0)
