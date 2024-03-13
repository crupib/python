from numpy import array
import matplotlib.pyplot as plt
from gram_schmidt import gram_schmidt

def curve(pos, col=(0, 0, 0)):
    plt.plot(*zip(*pos), color=col)

def draw_cube(o, x, y, z):
    axes, cols = [x, y, z], ['r', 'g', 'b']
    planes = [(y, z), (z, x), (x, y)]
    for ax, col, p in zip(axes, cols, planes):
        face = [o, o + p[0], o + p[0] + p[1], o + p[1]]
        for vertex in face:
            curve(pos=[vertex, vertex + ax], col=col)

o, e, u = array([0, 0, 0]), array([1, 2, 3]), array([5, 5, 5])
x, y, z = array([1, 0, 0]), array([0, 1, 0]), array([0, 0, 1])
E = array(gram_schmidt([e, x, y, z])[1:])
plt.axis('equal'), plt.axis('off')
for ax, lbl in [(x, "x'"), (y, "y'"), (z, "z'")]:
    curve(pos=[E.dot(-5 * ax), E.dot(10 * ax)], col=ax)
    plt.text(*E.dot(10 * ax), lbl, fontsize=24)
c1 = [u, 2*x, 2*y, 2*z]
c2 = [E.dot(v) for v in c1]
draw_cube(*c2), plt.show()
#plt.savefig('screen.png', bbox_inches='tight', pad_inches=0)
