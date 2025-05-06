# Softmax activation
import numpy as np

class Activation_Softmax: # Forward pass
  def forward(self, inputs):
          # Get unnormalized probabilities
      exp_values = np.exp(inputs - np.max(inputs, axis=1,
                                          keepdims=True))
      probabilities = exp_values / np.sum(exp_values, axis=1,
                                          keepdims=True)
      self.output = probabilities
def listdiv(lst, divisor):
  result = [[element / divisor for element in sublist] for sublist in lst]
  return result
softmax = Activation_Softmax()

softmax.forward([[1,2,3]])
print(softmax.output)

softmax.forward([[-2,-1,0]])
print(softmax.output)

lst = [[1,2,3]]
softmax.forward(listdiv(lst,2))
print(softmax.output)
