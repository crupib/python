from sympy import *
from numpy.random import seed, permutation
from functools import reduce

A = diag(1, 2, 2, 2, 2, 3, 3, 3, 3, 3)
A[1, 2] = A[3, 4] = A[5, 6] = A[7, 8] = A[8, 9] = 1

seed(123)
for n in range(10):
    P = permutation(10)
    for i, j in [(P[2 * k], P[2 * k + 1]) for k in range(5)]:
        A[:, j] += A[:, i]
        A[i, :] -= A[j, :]

B = Lambda(S('lmd'), A - S('lmd') * eye(10))
x = Matrix(var('x0, x1, x2, x3, x4, x5, x6, x7, x8, x9'))
y = Matrix(var('y0, y1, y2, y3, y4, y5, y6, y7, y8, y9'))
z = Matrix(var('z0, z1, z2, z3, z4, z5, z6, z7, z8, z9'))

a1 = x.subs(solve(B(1) * x))

a2 = x.subs(solve(B(2) * x))
b2 = y.subs(solve(B(2) * y - a2))

a3 = x.subs(solve(B(3) * x))
b3 = y.subs(solve(B(3) * y - a3))
c3 = z.subs(solve(B(3) * z - b3))

v0 = a1.subs({x9: 1})

v1 = b2.subs({y6: 1, y7: 0, y8: 0, y9: 0})
v2 = B(2) * v1

v3 = b2.subs({y6: 0, y7: 1, y8: 0, y9: 0})
v4 = B(2) * v3

v5 = c3.subs({z5: 1, z6: 0, z7: 0, z8: 0, z9: 0})
v6 = B(3) * v5
v7 = B(3) * v6

v8 = b3.subs({y6: 1, y7: 0, y8: 0, y9: 0})
v9 = B(3) * v8

if __name__ == '__main__':
    print(repr(A))
    L = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9]
    V = reduce(lambda V, v: V.row_join(v), L)
    print(repr(V))
    print(repr(V.inv() * A * V))
