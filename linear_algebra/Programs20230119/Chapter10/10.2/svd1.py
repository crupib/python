from numpy import array, diag, zeros
from numpy.linalg import pinv, svd

A = array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(pinv(A))
U1, S, U2 = svd(A)
Z = zeros((4, 2))
Z[:2, :2] = diag(S)
print(U1.dot(Z.dot(U2)))

'''
[[-1.00000000e+00 -5.00000000e-01  1.01325813e-15  5.00000000e-01]
 [ 8.50000000e-01  4.50000000e-01  5.00000000e-02 -3.50000000e-01]]
[[1. 2.]
 [3. 4.]
 [5. 6.]
 [7. 8.]]

'''
