from numpy.linalg import matrix_rank

def f(*x): return matrix_rank(x)

a, b, c = (1, 2), (2, 3), (2, 4)
print(f(a, b), f(b, c), f(a, c), f(a, b, c))
a, b, c, d = (1, 2, 3), (2, 3, 4), (3, 4, 5), (3, 4, 4)
print(f(a, b), f(a, b, c), f(a, b, d), f(a, b, c, d))

'''
2 2 1 2
2 2 3 3
'''
