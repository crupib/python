from sympy import Matrix, sin, cos, eye
from sympy.abc import theta

A = Matrix([[cos(theta), sin(theta)],
            [-sin(theta), cos(theta)]])
B = Matrix([[1,  0],
            [0, -1]])
C = Matrix([[cos(theta), -sin(theta)],
            [sin(theta), cos(theta)]])
D = C * B * A
E = (eye(2)+D) / 2
print(f'D = {D}')
print(f'E = {E}')

'''
D = Matrix([[-sin(theta)**2 + cos(theta)**2, 2*sin(theta)*cos(theta)], [2*sin(theta)*cos(theta), sin(theta)**2 - cos(theta)**2]])
E = Matrix([[-sin(theta)**2/2 + cos(theta)**2/2 + 1/2, sin(theta)*cos(theta)], [sin(theta)*cos(theta), sin(theta)**2/2 - cos(theta)**2/2 + 1/2]])
>>> D.simplify(); D
Matrix([
[cos(2*theta),  sin(2*theta)],
[sin(2*theta), -cos(2*theta)]])
>>> E.simplify(); E
Matrix([
[ cos(theta)**2, sin(2*theta)/2],
[sin(2*theta)/2,  sin(theta)**2]])
'''
