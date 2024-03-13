from sympy import solve
from sympy.abc import a, b, x, y, z

ans = solve([a + 2*b - x, 2*a + 3*b - y, 3*a + 4*b - z], [a, b])
print(ans)

'''
[]
>>> ans = solve([a + 2*b - x, 2*a + 3*b - y, 3*a + 4*b - z], [a, b, x])
>>> ans
{a: -4*y + 3*z, b: 3*y - 2*z, x: 2*y - z}
'''
