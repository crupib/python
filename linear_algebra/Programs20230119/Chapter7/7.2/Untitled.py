from sympy import *
A = Matrix([[3, -4, 2], [2, -3, 2], [3, -6, 4]])
f = det(A - var('lmd') * eye(3))

'''
>>> f
-lmd**3 + 4*lmd**2 - 5*lmd + 2
>>> factor(f)
-(lmd - 2)*(lmd - 1)**2
>>> v = Matrix([var('x'), var('y'), var('z')]); v
Matrix([
[x],
[y],
[z]])
>>> w = Lambda(lmd, (A - lmd * eye(3)) * v); w
Lambda(lmd, Matrix([
[ x*(3 - lmd) - 4*y + 2*z],
[2*x + y*(-lmd - 3) + 2*z],
[ 3*x - 6*y + z*(4 - lmd)]]))
>>> ans = solve(w(1)); ans
{x: 2*y - z}
>>> ans = solve(w(2)); ans
{x: 2*z/3, y: 2*z/3}
>>> A.eigenvals()
{2: 1, 1: 2}
>>> A.eigenvects()
[(1, 2, [Matrix([
[2],
[1],
[0]]), Matrix([
[-1],
[ 0],
[ 1]])]), (2, 1, [Matrix([
[2/3],
[2/3],
[  1]])])]
'''
