from sympy import symbols

x, y = symbols('x y')
expr = (x + y) ** 2

result = expr.expand().subs(x, y)
print(result)
