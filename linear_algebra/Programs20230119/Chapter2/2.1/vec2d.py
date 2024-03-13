from numpy import array
import matplotlib.pyplot as plt

o, x, y = array([0, 0]), array([3, 2]), array([1, 2])
arrows = [(o, x + y, 'b'), (o, x, 'r'), (x, y, 'g'),
          (o, y, 'g'), (y, x, 'r')]
for p, v, c in arrows:
    plt.quiver(p[0], p[1], v[0], v[1],
               color=c, units='xy', scale=1)
plt.axis('scaled'), plt.xlim(0, 5), plt.ylim(0, 5), plt.show()
