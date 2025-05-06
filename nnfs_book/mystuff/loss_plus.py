import numpy as np
import nnfs
from nnfs.datasets import spiral_data
nnfs.init()
# Dense layer
class Layer_Dense:
      # Layer initialization
  def __init__(self, n_inputs, n_neurons):
     self.weights = 0.01 * np.random.randn(n_inputs, n_neurons) 
     self.biases = np.zeros((1, n_neurons))
  def forward(self, inputs):
    self.output = np.dot(inputs, self.weights) + self.biases
  # ReLU activation
class Activation_ReLU:
  def forward(self, inputs):
    self.output = np.maximum(0, inputs)
class Activation_Softmax: # Forward pass
  def forward(self, inputs):
     exp_values = np.exp(inputs - np.max(inputs, axis=1,
                                         keepdims=True))
     probabilities = exp_values / np.sum(exp_values, axis=1,keepdims=True)
     self.output = probabilities
# Common loss class
class Loss:
  def calculate(self, output, y):
      sample_losses = self.forward(output, y)
      data_loss = np.mean(sample_losses)
      return data_loss
# Cross-entropy loss
class Loss_CategoricalCrossentropy(Loss): # Forward pass
  def forward(self, y_pred, y_true): # Number of samples in a batch
      samples = len(y_pred)
      y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)
      if len(y_true.shape) == 1:
         correct_confidences = y_pred_clipped[
               range(samples),
               y_true ]
        # Mask values - only for one-hot encoded labels
      elif len(y_true.shape) == 2:
            correct_confidences = np.sum(
                  y_pred_clipped*y_true,
                  axis=1 )
      negative_log_likelihoods = -np.log(correct_confidences)
      return negative_log_likelihoods
X, y = spiral_data(samples=100, classes=3)
dense1 = Layer_Dense(2, 3)
activation1 = Activation_ReLU()
dense2 = Layer_Dense(3, 3)
activation2 = Activation_Softmax()
loss_function = Loss_CategoricalCrossentropy()
dense1.forward(X)
activation1.forward(dense1.output)
dense2.forward(activation1.output)
activation2.forward(dense2.output)
print(activation2.output[:5])
loss = loss_function.calculate(activation2.output, y)
print('loss:', loss)
predictions = np.argmax(activation2.output, axis=1)
if len(y.shape) == 2:
   y = np.argmax(y, axis=1)
accuracy = np.mean(predictions == y)
  # Print accuracy
print('acc:', accuracy)
