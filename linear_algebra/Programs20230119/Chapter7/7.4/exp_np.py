from numpy import matrix, e, exp, diag
from numpy.linalg import eigh

A = matrix([[1, 2], [2, 1]])
m, B = 1, 0
for n in range(10):
    B += A ** n / m
    m *= n + 1
print(B)

a = eigh(A)
S, V = diag(e**a[0]), a[1] 
print(V * S * V.H)

print(exp(A))


'''
[[10.21563602  9.84775683]
 [ 9.84775683 10.21563602]]
[[10.22670818  9.85882874]
 [ 9.85882874 10.22670818]]
[[2.71828183 7.3890561 ]
 [7.3890561  2.71828183]]
'''
