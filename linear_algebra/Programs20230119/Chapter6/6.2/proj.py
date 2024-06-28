from numpy import random, array, inner, sqrt, dot
import matplotlib.pyplot as plt

random.seed(2021)
v = array([3, 4])
e =  v / sqrt(inner(v, v))
plt.axis('scaled'), plt.xlim(-10, 10), plt.ylim(-10, 10)
for n in range(100):
    v = random.uniform(-10, 10, 2)
    plt.scatter(*v)
    w = inner(e, v) * e
    #P = dot(e.reshape((2, 1)), e.reshape((1, 2)))
    #w = dot(P, v)
    plt.plot(*zip(v, w))
plt.show()
#plt.savefig('proj.png', bbox_inches='tight', pad_inches=0)
