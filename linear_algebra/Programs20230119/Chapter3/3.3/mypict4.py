from vpython import canvas, vec, curve, arrow, color, points
from numpy import array, linspace, sin, cos, pi, random

canvas(background=color.white, foreground=color.black)
for v in [vec(1, 0, 0), vec(0, 1, 0), vec(0, 0, 1)]:
    curve(pos=[-v, v], color=v)

with open('mypict1.txt', 'r') as fd:
    XY = eval(fd.read())

random.seed(123)
a = vec(*random.normal(0, 1, 3))
arrow(pos=vec(0, 0, 0), axis=a, shaftwidth=0.1)
b = vec(*random.normal(0, 1, 3))
arrow(pos=vec(0, 0, 0), axis=b, shaftwidth=0.1)
P = [x * a + y * b for (x, y) in XY]
Q = [cos(t) * a + sin(t) * b for t in linspace(0, 2 * pi, 101)]
points(pos=P, radius=2, color=color.cyan)
curve(pos=Q, color=color.magenta)
