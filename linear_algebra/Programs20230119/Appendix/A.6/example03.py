import sympy
from sympy.abc import x, y

ans1 = sympy.solve([x + 2*y - 1, 4*x + 5*y - 2])
print(ans1)
ans2 = sympy.solve([x**2 + x + 1])
print(ans2)
ans3 = sympy.solve([x**2 + y**2 - 1, x - y])
print(ans3)

'''
{x: -1/3, y: 2/3}
[{x: -1/2 - sqrt(3)*I/2}, {x: -1/2 + sqrt(3)*I/2}]
[{x: -sqrt(2)/2, y: -sqrt(2)/2}, {x: sqrt(2)/2, y: sqrt(2)/2}]
'''
