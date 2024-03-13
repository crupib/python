from numpy import linspace, exp, sqrt
from numpy.polynomial.legendre import Legendre
from numpy.polynomial.chebyshev import Chebyshev
from numpy.polynomial.laguerre import Laguerre
from numpy.polynomial.hermite import Hermite
import matplotlib.pyplot as plt

x1 = linspace(-1, 1, 1001)
x2 = x1[1:-1]
x3 = linspace(0, 10, 1001)
x4 = linspace(-3, 3, 1001)

f, x, w = Legendre, x1, 1
# f, x, w = Chebyshev, x2, 1
# f, x, w = Chebyshev, x2, 1/sqrt(1 - x2**2)
# f, x, w = Laguerre, x3, 1
# f, x, w = Laguerre, x3, exp(-x3)
# f, x, w = Hermite, x4, 1
#f, x, w = Hermite, x4, exp(-x4**2)
for n in range(6):
    e = f.basis(n)(x)
    plt.plot(x, e * w)
plt.show()
#plt.savefig('Legendre_np2.png', bbox_inches='tight', pad_inches=0)
