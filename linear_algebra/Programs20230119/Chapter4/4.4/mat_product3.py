from sympy import Matrix, solve, eye
from sympy.abc import a, b, c, d, e, f

A = Matrix([[1, 2, 3], [2, 3, 4]])
B = Matrix([[a, b], [c, d], [e, f]])
ans = solve(A*B - eye(2), [a, b, c, d, e, f])
print(ans)


'''
{a: e - 3, c: 2 - 2*e, b: f + 2, d: -2*f - 1}
>>> C = B.subs(ans); C
Matrix([
[  e - 3,    f + 2],
[2 - 2*e, -2*f - 1],
[      e,        f]])
>>> A * C
Matrix([
[1, 0],
[0, 1]])
'''
