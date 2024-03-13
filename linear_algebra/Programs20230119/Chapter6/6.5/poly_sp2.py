from sympy.polys.orthopolys import (
    legendre_poly,
    chebyshevt_poly,
    chebyshevu_poly,
    laguerre_poly,
    hermite_poly,
)
from sympy.abc import x

e = legendre_poly
for n in range(4):
    print(f'e{n}(x) = {e(n, x)}')

'''
e0(x) = 1
e1(x) = x
e2(x) = 3*x**2/2 - 1/2
e3(x) = 5*x**3/2 - 3*x/2
'''
