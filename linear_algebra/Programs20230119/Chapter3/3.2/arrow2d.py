import matplotlib.pyplot as plt

o, a, b, c = (0, 0), (1, 2), (2, 3), (2, 4)
arrows = [[o, a, 'r', 0.1], [o, b, 'g', 0.05], [o, c, 'b', 0.05]]
plt.axis('scaled'), plt.xlim(0, 5), plt.ylim(0, 5)
for p, v, c, w in arrows:
    plt.quiver(p[0], p[1], v[0], v[1],
               units='xy', scale=1, color=c, width=w)

plt.show()
