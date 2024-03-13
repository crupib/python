from sympy import Matrix, Symbol, factor_list, factor
from numpy.random import choice, seed

seed(2021)
D = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

def f():
    while True:
        A = Matrix(choice(D, (3, 3)))
        cp = A.charpoly(Symbol('lmd'))
        F = factor_list(cp)
        if len(F[1]) == 3:
            print(f'det(A - lmd*I) = {factor(cp.expr)}\nA = {A}')
            return A

'''
det(A - lmd*I) = lmd*(lmd - 2)*(lmd + 4)
A = Matrix([[5, -5, -1], [3, -2, -2], [4, -1, -5]])
Matrix([
[5, -5, -1],
[3, -2, -2],
[4, -1, -5]])
'''
