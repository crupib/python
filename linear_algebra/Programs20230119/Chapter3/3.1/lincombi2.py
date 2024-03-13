from vpython import vec, arrow, curve, color, points
from numpy.random import normal, seed

seed(123)
o = vec(0, 0, 0)
e1, e2, e3 = vec(1, 0, 0), vec(0, 1, 0), vec(0, 0, 1)
curve(pos=[-3*e1, 3*e1], color=color.cyan)
curve(pos=[-3*e2, 3*e2], color=color.magenta)
curve(pos=[-3*e3, 3*e3], color=color.yellow)
x = vec(*normal(0, 1, 3))
arrow(pos=vec(0, 0, 0), axis=x, color=color.red)
y = vec(*normal(0, 1, 3))
arrow(pos=vec(0, 0, 0), axis=y, color=color.green)
W = [a * x + b * y for (a, b) in normal(0, 1, (1000, 2))]
points(pos=W, radius=2)
