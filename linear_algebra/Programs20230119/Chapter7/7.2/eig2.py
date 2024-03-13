import numpy as np

A = [[1, 1], [0, 1]]
b = np.linalg.eig(A)
print(f'''eigen values: {b[0][0]}, {b[0][1]}
eigen vectors:
{b[1][:, 0]}
{b[1][:, 1]}''')

'''
eigen values: 1.0, 1.0
eigen vectors:
[1. 0.]
[-1.00000000e+00  2.22044605e-16]
'''
