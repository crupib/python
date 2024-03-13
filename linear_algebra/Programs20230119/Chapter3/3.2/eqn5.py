from sympy import solve
from sympy.abc import x, y

ans = solve([x + 2*y, 2*x + 4*y], [x, y])
print(ans)

'''
{x: -2*y}
'''
