from sympy import Matrix
from numpy.random import choice, seed

N = [-3, -2, -1, 1, 2, 3]
seed(2021)

def f(truth):
    while True:
        A = Matrix(choice(N, (2, 2)))
        eigenvals= A.eigenvals()
        if len(eigenvals) == 2 and not 0 in eigenvals:
            if all([x.is_real for x in eigenvals]) == truth:
                print(eigenvals)
                return A

'''
>>> f(True)
{3 - sqrt(2): 1, sqrt(2) + 3: 1}
Matrix([
[3, 2],
[1, 3]])
>>> f(False)
{5/2 - sqrt(35)*I/2: 1, 5/2 + sqrt(35)*I/2: 1}
Matrix([
[ 3, 3],
[-3, 2]])
'''
