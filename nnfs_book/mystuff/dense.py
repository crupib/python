import numpy as np
import nnfs
nnfs.init()
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data
class Layer_Dense:
  def __init__(self, n_inputs,n_neurons):
      self.weights = 0.01*np.random.randn(n_inputs,n_neurons)
      self.biases = np.zeros((1,n_neurons))
  def forward(self,inputs):
      self.output = np.dot(inputs, self.weights) + self.biases
nnfs.init()
n_inputs = 2
n_neurons = 4
X,y = spiral_data(samples=100, classes=3)
dense1 = Layer_Dense(2,3)
dense1.forward(X)
print(dense1.output[:5])
