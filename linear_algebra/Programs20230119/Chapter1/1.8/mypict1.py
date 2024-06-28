import PIL.Image as Img
from numpy import array

A = array(Img.open('mypict1.jpg'))
B = A < 200
m, n = B.shape
h = max(m, n)
x0, y0 = m / h, n / h

def f(i, j):
    return (y0 * (-1 + 2 * j / (n - 1)), x0 * (1 - 2 * i / (m - 1)))

P = [f(i, j) for i in range(m) for j in range(n) if B[i, j]]
with open('mypict1.txt', 'w') as fd:
    fd.write(repr(P))

'''
>>> B
array([[False, False, False, ..., False,  True, False],
       [False, False, False, ...,  True,  True, False],
       [False, False, False, ...,  True,  True, False],
       ...,
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False]])
S'''
