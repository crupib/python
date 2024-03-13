import sympy as sp

A = [[1, 1], [0, 1]]
a = sp.Matrix(A).eigenvects()
print(f'''eigen value: {a[0][0]}
multiplicity: {a[0][1]}
eigen vector:
{a[0][2][0]}''')

'''
eigen value: 1
multiplicity: 2
eigen vector:
Matrix([[1], [0]])
'''
