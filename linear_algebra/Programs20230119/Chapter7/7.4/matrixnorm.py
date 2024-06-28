from numpy import array, arange, pi, sin, cos
from numpy.linalg import eig, norm

M = [array([[1, 2], [2, 1]]),
     array([[1, 2], [-2, 1]]),
     array([[1, 2], [3, 4]])]
T = arange(0, 2 * pi, pi / 500)
U = array([(cos(t), sin(t)) for t in T])
for A in M:
    r1 = max([abs((A.dot(u)).dot(u)) for u in U])
    r2 = max([abs(e) for e in eig(A)[0]])
    r3 = max([norm(A.dot(u)) for u in U])
    print(f'{A}: num={r1:.2f}, spec={r2:.2f}, norm={r3:.2f}')

'''
[[1 2]
 [2 1]]: num=3.00, spec=3.00, norm=3.00
[[ 1  2]
 [-2  1]]: num=1.00, spec=2.24, norm=2.24
[[1 2]
 [3 4]]: num=5.42, spec=5.37, norm=5.46
'''
