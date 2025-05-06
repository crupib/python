import numpy as np
import nnfs
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data
class Layer_Dense:
  def __init__(self, n_inputs, n_neurons):
    self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
    self.biases = np.zeros((1,n_neurons))
  def forward(self,inputs):
    self.output = np.dot(inputs,self.weights) + self.biases
nnfs.init()
X,y = spiral_data(samples=100, classes=3)
dense1 = Layer_Dense(2,3)
dense1.forward(X)
print(dense1.output[:5])
#plt.scatter(X[:,0],X[:,1],c=y, cmap='brg')
#plt.show()
#print(np.random.randn(2,5))
#print(np.zeros((2,5)))
