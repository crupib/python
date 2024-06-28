from vpython import *

Ball = sphere(color=color.red)
Wall = box(pos=vec(-10, 0, 0), length=1, width=10, height=10)
Spring = helix(pos=vec(-10, 0, 0), length=10)
dt, x, v = 0.01, 2.0, 0.0
while True:
    rate(1 / dt)
    dx, dv = v * dt, -x * dt
    x, v = x + dx, v + dv
    Ball.pos.x, Spring.length = x, 10 + x

