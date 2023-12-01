import numpy as np

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.matrix(A))
transpose_A = [list(i) for i in zip(*A)]
print()
print(np.matrix(transpose_A))
