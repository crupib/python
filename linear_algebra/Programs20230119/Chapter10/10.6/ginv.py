from sympy import *
s = Symbol(r'\sigma', positive=True)
t = Symbol(r'\tau', positive=True)
A = Matrix([[s, 0, t, 0], [0, s, 0, t]])

B = A.pinv()
print(latex(simplify(B)))

'''
\left[\begin{matrix}\frac{\sigma}{\sigma^{2} + \tau^{2}} & 0\\0 & \frac
{\sigma}{\sigma^{2} + \tau^{2}}\\\frac{\tau}{\sigma^{2} + \tau^{2}} &
0\\0 & \frac{\tau}{\sigma^{2} + \tau^{2}}\end{matrix}\right]
'''
