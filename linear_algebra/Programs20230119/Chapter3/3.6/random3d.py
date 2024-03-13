from vpython import canvas, color, vec, curve, points
from numpy.random import normal

canvas(background=color.white, foreground=color.black)
for v in [vec(5, 0, 0), vec(0, 5, 0), vec(0, 0, 5)]:
    curve(pos=[-v, v], color=v)
P = normal(0, 1, (1000, 3))
points(pos=[vec(*p) for p in P], radius=4)
