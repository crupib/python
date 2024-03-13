from numpy import array, sqrt, trace, diag, linalg

A = array([[1, 2], [3, 4]])
U, S, V = linalg.svd(A)
A1 = V.T.dot(diag(S).dot(V))

print(trace(A1))
print(S.sum())
print(linalg.norm(A, ord='nuc'))

print(sqrt(trace(A.T.dot(A))))
print(sqrt((A**2).sum()))
print(linalg.norm(A, ord='fro'))

print(S.max()/S.min())
print(linalg.cond(A))
B = linalg.inv(A)
print(linalg.norm(A, ord=2)*linalg.norm(B, ord=2))

'''
5.830951894845301
5.8309518948453
5.8309518948453
5.477225575051661
5.477225575051661
5.477225575051661
14.933034373659265
14.933034373659265
14.93303437365925
'''
