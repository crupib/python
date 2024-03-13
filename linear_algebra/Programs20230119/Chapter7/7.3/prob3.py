from sympy import Matrix
from numpy.random import choice, seed

seed(2021)
N = [-3, -2, -1, 1, 2, 3]


def g(symmetric=True):
    if symmetric:
        a, b, d = choice(N, 3)
        return Matrix([[a, b], [b, d]])
    else:
        a, b = choice(N, 2)
        return Matrix([[a, b], [-b, a]])

'''
>>> g()
Matrix([
[2,  3],
[3, -2]])
>>> g(False)
Matrix([
[-3,  3],
[-3, -3]])
'''
