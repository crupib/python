from sympy import solve
from sympy.abc import x, y, z

ans1 = solve([x + 2*y + 3*z, 2*x + 3*y + 4*z, 3*x + 4*y + 5*z],
             [x, y, z])
print(ans1)

ans2 = solve([x + 2*y + 3*z, 2*x + 3*y + z, 3*x + y + 2*z],
             [x, y, z])
print(ans2)

'''
{x: z, y: -2*z}
{x: 0, y: 0, z: 0}
'''
