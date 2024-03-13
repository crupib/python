import numpy as np
import matplotlib.pyplot as plt

cutoff = 14
N = 60000
with open('train-images.bin', 'rb') as fd:
    X = np.fromfile(fd, 'uint8', -1)[16:]
X = X.reshape((N, 28, 28))
with open('train-labels.bin', 'rb') as fd:
    Y = np.fromfile(fd, 'uint8', -1)[8:]
D = {y: [] for y in set(Y)}
for x, y in zip(X, Y):
    D[y].append(x)

A = sum([x.astype('float') for x in X]) / N
U, Sigma, V = np.linalg.svd(A)
print(Sigma)

def proj(X, U, V, k):
    U1, V1 = U[:, :k], V[:k, :]
    P, Q = U1.dot(U1.T), V1.T.dot(V1)
    return P.dot(X.dot(Q))


fig, axs = plt.subplots(10, 10, figsize=(10, 10))
for y in D:
    for k in range(10):
        ax = axs[y][k]
        A = D[y][k]
        B = proj(A, U, V, cutoff)
        ax.imshow(255 - B, 'gray')
        ax.tick_params(labelbottom=False, labelleft=False,
                       color='white')
plt.show()
#plt.savefig(f'mnist{cutoff}.png', bbox_inches='tight', pad_inches=0.05)
