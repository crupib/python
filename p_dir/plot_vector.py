import numpy as np
import matplotlib.pyplot as plt
v = np.array([1,-2])
v1 = np.array([-1,-1])
v3 = np.array([2,0])
plt.plot([0,v[0]],[0,v[1]])
plt.plot([-2,v1[0]],[1,v1[1]])
plt.plot([1,v3[0]],[2,v3[1]])
plt.axis([-3,3,-3,3])
plt.grid()
plt.show()
