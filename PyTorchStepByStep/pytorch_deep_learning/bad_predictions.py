import numpy as np
np.random.seed(42)
b = np.random.randn(1)
w = np.random.randn(1)
N = 100
x = np.random.rand(N,1)
idx = np.arange(N)
np.random.shuffle(idx)
train_idx = idx[:int(N*0.8)]
val_idx = idx[int(N*0.8):]
x_train = x[train_idx]
yhat = b+w * x_train
print(yhat)
