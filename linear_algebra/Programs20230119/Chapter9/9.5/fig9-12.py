from numpy import *
from pyx import *

unit.set(uscale=0.5, vscale=0.5, wscale=2, xscale=0.5)
C = canvas.canvas()

N = 10
d = 5
state = [color.grey.white, color.grey.black]

for i in range(N):
    y = i * d
    C.stroke(path.line(0, y, (N - 1) * d, y))
    for j in range(N):
        x = j * d
        C.stroke(path.line(x, 0, x, (N  - 1) * d))

for i in range(N - 1):
    y0 = i * d
    y1 = (i + 1) * d
    C.stroke(path.line(0, y, (N - 1) * d, y))
    for j in range(N - 1):
        x0 = j * d
        x1 = (j + 1) * d
        C.stroke(path.line(x0, y0, x1, y1))
        C.stroke(path.line(x0, y1, x1, y0))

for i in range(N):
    y = i * d
    for j in range(N):
        x = j * d
        s = random.randint(0, 2)
        C.stroke(path.circle(x, y, 1), [deco.filled([state[s]])])

C.writePDFfile('fig9-12.pdf')


