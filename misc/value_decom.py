#importing the scipy and numpy packages
from scipy import linalg
import numpy as np

#Declaring the numpy array
a = np.random.randn(3, 2) + 1.j*np.random.randn(3, 2)

#Passing the values to the eig function
U, s, Vh = linalg.svd(a)

# printing the result
print("U")
print("-----------")
print (U)
print("VH")
print("-----------")
print (Vh)
print("s")
print("-----------")
print(s)
