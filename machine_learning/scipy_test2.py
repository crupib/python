from scipy import sparse
import numpy as np

eye = np.eye(4)
sparse_matrix = sparse.csr_matrix(eye)

print("\nSciPy sparse CSR Matrix:\n{}".format(sparse_matrix))

