from sympy import integrate, sqrt, exp, oo
from sympy.abc import x

D = {
    'Ledendre': ((x, -1, 1), 1),
    'Chebyshev1': ((x, -1, 1), 1 / sqrt(1 - x**2)),
    'Chebyshev2': ((x, -1, 1), sqrt(1 - x**2)),
    'Laguerre': ((x, 0, oo), exp(-x)),
    'Hermite': ((x, -oo, oo), exp(-x**2)),
}
dom, weight = D['Ledendre']


def inner(expr1, expr2):
    return integrate(expr1*expr2*weight, dom)


def gram_schmidt(A):
    E = []
    while A != []:
        a = A.pop(0)
        b = a - sum([inner(e, a) * e for e in E])
        c = sqrt(inner(b, b))
        E.append(b / c)
    return E

E = gram_schmidt([1, x, x**2, x**3])
for n, e in enumerate(E):
    print(f'e{n}(x) = {e}')

'''
e0(x) = sqrt(2)/2
e1(x) = sqrt(6)*x/2
e2(x) = 3*sqrt(10)*(x**2 - 1/3)/4
e3(x) = 5*sqrt(14)*(x**3 - 3*x/5)/4
'''
