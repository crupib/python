import matplotlib.pyplot as plt
from numpy.random import normal

P = normal(0, 1, (1000, 2))
plt.scatter(P[:, 0], P[:, 1], s=4)
plt.axis('equal'), plt.show()