import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
x = np.linspace(-10,10,100)
y = np.sin(x)
plt.plot(x,y,marker="x")

