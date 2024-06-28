from vpython import vec, arrow, color, points
from numpy.random import normal

x = vec(*normal(0, 1, 3))
arrow(pos=vec(0, 0, 0), axis=x, color=color.red)
y = vec(*normal(0, 1, 3))
arrow(pos=vec(0, 0, 0), axis=y, color=color.red)
W = [a * x + b * y for (a, b) in normal(0, 1, (1000, 2))]
points(pos=W, radius=2)
