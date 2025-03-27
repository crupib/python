import numpy as np
true_b = 1
true_w = 2
N = 100
np.random.seed(42)
x = np.random.rand(N,1)
epsilon = (0.1 * np.random.randn(N,1))
y = true_b + true_w * x + epsilon
idx = np.arange(N)
np.random.shuffle(idx)
train_idx = idx[:int(N*0.8)]
val_idx = idx[int(N*0.8):]
x_train, y_train = x[train_idx], y[train_idx]
x_val, y_val = x[val_idx], y[val_idx]
print("X Train")
print("*******")
print(x_train)
print("Y Train")
print("*******")
print(y_train)
print("X val")
print("*******")
print(x_val)
print("Y val")
print("*******")
print(y_val)
