from numpy.linalg import eigh
from scatter import data, scatter2d, scatter3d

n = len(data)
mean = sum(data) / n
C = data - mean
A = C.T
AAt = A.dot(C) / n
E, U = eigh(AAt)
print(E)
#scatter3d(C.dot(U))
scatter2d(C.dot(U), 'principal2d')
