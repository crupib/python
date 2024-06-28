from sympy import solve
from sympy.abc import a, b, x, y

ans = solve([a + 2*b - x, 2*a + 3*b - y], [a, b])
print(ans)

'''
{a: -3*x + 2*y, b: 2*x - y}
>>> ans[a]
-3*x + 2*y
>>> ans[b]
2*x - y
'''
