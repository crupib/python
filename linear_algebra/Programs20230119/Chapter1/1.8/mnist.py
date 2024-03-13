import numpy as np
import matplotlib.pyplot as plt

N = 10000
with open('test-images.bin', 'rb') as f1:
    X = np.fromfile(f1, 'uint8', -1)[16:]
X = X.reshape((N, 28, 28))
with open('test-labels.bin', 'rb') as f2:
    Y = np.fromfile(f2, 'uint8', -1)[8:]
D = {y: [] for y in set(Y)}
for x, y in zip(X, Y):
    D[y].append(x)
print([len(D[y]) for y in sorted(D)])

fig, ax = plt.subplots(11, 10, figsize=(10, 10))
plt.subplots_adjust(wspace=0.1, hspace=0.1,
                    left=0.01, right=0.99, bottom=0.01, top=0.99)
for y in D:
    for k in range(10):
        A = 255 - D[y][k]
        ax[k][y].imshow(A, 'gray')
        ax[k][y].tick_params(labelbottom=False, labelleft=False,
                             color='white')
    A = 255 - sum([x.astype('float') for x in D[y]]) / len(D[y])
    ax[10][y].imshow(A, 'gray')
    ax[10][y].tick_params(labelbottom=False, labelleft=False,
                          color='white')
plt.show()
#plt.savefig('mnist.pdf')
