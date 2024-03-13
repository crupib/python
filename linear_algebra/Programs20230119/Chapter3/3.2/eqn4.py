from sympy import solve
from sympy.abc import x, y

ans = solve([x + 2*y, 2*x + 3*y], [x, y])
print(ans)

'''
{x: 0, y: 0}
'''
