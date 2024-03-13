from numpy.random import seed, randint, choice
from sympy import Matrix, latex

seed(2021)
m, n = randint(2, 4, 2)
X = [-3, -2, -1, 1, 2, 3, 4, 5]
A = Matrix(choice(X, (m, n)))
B = Matrix(choice(X, (m, n)))
print(f'{latex(A)} + {latex(B)} = ')

'''
\left[\begin{matrix}-2 & -3 & 3\\4 & 4 & 2\end{matrix}\right] + \left[\begin{matrix}5 & 4 & 1\\3 & 3 & 3\end{matrix}\right] = 
'''
