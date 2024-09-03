import numpy as np
layer_outputs = np.array([[4.8, 1.21, 2.385],
                          [8.9, -1.81, 0.2],
                          [1.41, 1.051, 0.026]])
print('Sum without axis')
print(np.sum(layer_outputs))

print('This will be identical to the above since default is None:')
print(np.sum(layer_outputs, axis=None))

print('Another way to think of it w/ a matrix == axis 0: columns:')
print(np.sum(layer_outputs, axis=0))

print('But we want to sum the rows instead, like this w/ raw py:')
for i in layer_outputs:
    print(sum(i))

print('So we can sum axis 1, but note the current shape:') 
print(np.sum(layer_outputs, axis=1))

print('Sum axis 1, but keep the same dimensions as input:') 
print(np.sum(layer_outputs, axis=1, keepdims=True))
