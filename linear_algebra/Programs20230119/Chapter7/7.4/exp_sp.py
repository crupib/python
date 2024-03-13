from sympy import Matrix, exp, var
var('n')

A = Matrix([[1, 2], [2, 1]])
print(A**n)
print(exp(A))

'''
Matrix([[(-1)**n/2 + 3**n/2, -(-1)**n/2 + 3**n/2], [-(-1)**n/2 + 3**n/2, (-1)**n/2 + 3**n/2]])
Matrix([[exp(-1)/2 + exp(3)/2, -exp(-1)/2 + exp(3)/2], [-exp(-1)/2 + exp(3)/2, exp(-1)/2 + exp(3)/2]])
'''
