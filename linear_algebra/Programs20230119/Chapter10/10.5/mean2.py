import numpy as np
import matplotlib.pyplot as plt

N = 60000
with open('train-images.bin', 'rb') as fd:
    X = np.fromfile(fd, 'uint8', -1)[16:]
X = X.reshape((N, 28, 28))
with open('train-labels.bin', 'rb') as fd:
    Y = np.fromfile(fd, 'uint8', -1)[8:]
D = {y: [] for y in set(Y)}
for x, y in zip(X, Y):
    D[y].append(x)
print([len(D[y]) for y in sorted(D)])


A = 255 - sum([x.astype('float') for x in X]) / N
plt.tick_params(labelbottom=False, labelleft=False,
                color='white')
plt.imshow(A, 'gray')
#plt.show()
plt.savefig('mean2.pdf', bbox_inches='tight', pad_inches=0.05)
