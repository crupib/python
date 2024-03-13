from sympy import solve
from sympy.abc import a, b, c, x, y, z

ans = solve([a + 2*b + 3*c - x, 2*a + 3*b + c - y,
             3*a + 4*b + 2*c - z], [a, b, c])

print(ans)

'''
{a: -2*x/3 - 8*y/3 + 7*z/3, b: x/3 + 7*y/3 - 5*z/3, c: x/3 - 2*y/3 + z/3}
>>> N = [ans[k].subs([[x, 2], [y, 3], [z, 5]]) for k in [a, b, c]]; N
[7/3, -2/3, 1/3]
>>> [n.evalf(2) for n in N]
[2.3, -0.67, 0.33]
'''
