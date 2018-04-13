import matplotlib.pyplot as plt
import numpy as np
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
x = np.linspace(-10,10,100)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,marker="x")
plt.plot(x,z,marker="x")

