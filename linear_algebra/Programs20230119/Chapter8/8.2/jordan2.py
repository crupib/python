from sympy import Matrix, diag
from numpy.random import permutation, seed

X = Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 2]])
Y = Matrix([[2, 1, 0], [0, 2, 1], [0, 0, 2]])
Z = Matrix([[2, 1, 0], [0, 2, 0], [0, 0, 2]])

seed(2021)
while True:
    A = X.copy()
    while 0 in A:
        i, j, _  = permutation(3)
        A[:, j] += A[:, i]
        A[i, :] -= A[j, :]
        if max(abs(A)) >= 10:
            break
    if max(abs(A)) < 10:
        break
U, J = A.jordan_form()
print(f'A = {A}')
print(f'U = {U}')
print(f'U**(-1)*A*U = {J}')
C = U * diag(J[0, 0], J[1, 1], J[2, 2]) * U**(-1)
B = A - C
print(f'B = {B}')
print(f'C = {C}')


'''
A = Matrix([[2, 4, 4], [-4, 3, -1], [2, -4, -1]])
U = Matrix([[24/7, -4/7, -1/2], [30/7, 1, -1], [-36/7, 0, 1]])
U**(-1)*A*U = Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 2]])
B = Matrix([[8, 8, 12], [10, 10, 15], [-12, -12, -18]])
C = Matrix([[-6, -4, -8], [-14, -7, -16], [14, 8, 17]])
'''
