from vpython import *
import numpy as np

o = vec(0, 0, 0)
x, y, z = vec(1, 0, 0), vec(0, 1, 0), vec(0, 0, 1)
yz, zx, xy = [o, y, z, y+z], [o, z, x, z+x], [o, x, y, x+y]

def T(A, u): return vec(*np.dot(A, (u.x, u.y, u.z)))

E1 = [[1, 2, 0], [0, 1, 0], [0, 0, 1]]
E2 = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
E3 = [[2, 0, 0], [0, 1, 0], [0, 0, 1]]

def draw(E, filename):
    scene = canvas(width=600, height=600)
    scene.camera.pos = vec(3, 4, 5)
    scene.camera.axis = -vec(3, 4, 5)
    box(pos=(x+y+z)/2)
    for axis in [x, y, z]:
        curve(pos=[-axis, 3*axis], color=axis)
    for axis, face in [(x, yz), (y, zx), (z, xy)]:
        for side in face:
            A = E
            curve(pos=[T(A, side), T(A, axis+side)], color=axis)
    scene.capture(filename)

draw(E1, 'E1')
