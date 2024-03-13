from numpy import array
from numpy.random import randint, seed

seed(2021)
N = [1, 2, 3, 4, 5, 6]
Omega = [(w1, w2)  for w1 in N for w2 in N]

def omega():
    return Omega[randint(len(Omega))]

def P(w):
    return 1 / len(Omega)

def X(w):
    return array([w[0] + w[1], w[0] - w[1]])

def E(X):
    return sum([X(w) * P(w) for w in Omega])

for n in range(5):
    w = omega()
    print(X(w), end=' ')
print(f'\nE(X)={E(X)}')

'''
[8 0] [2 0] [7 5] [ 9 -1] [9 1] 
E(X)=[ 7.00000000e+00 -8.32667268e-17]
'''
