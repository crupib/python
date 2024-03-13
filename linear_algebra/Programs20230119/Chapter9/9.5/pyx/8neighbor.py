from numpy import *
from pyx import *

p = 0.1 / 0.5

C = canvas.canvas([trafo.scale(sx=1, sy=1)])

N = 10
d = 5
state = [color.grey.white, color.grey.black]

for i in range(N):
    y = i * d
    C.stroke(path.line(0 * p, y * p, (N - 1) * d * p, y * p))
    for j in range(N):
        x = j * d
        C.stroke(path.line(x * p, 0 * p, x * p, (N  - 1) * d * p))

for i in range(N - 1):
    y0 = i * d
    y1 = (i + 1) * d
    C.stroke(path.line(0 * p, y * p, (N - 1) * d * p, y * p))
    for j in range(N - 1):
        x0 = j * d
        x1 = (j + 1) * d
        C.stroke(path.line(x0 * p, y0 * p, x1 * p, y1 * p))
        C.stroke(path.line(x0 * p, y1 * p, x1 * p, y0 * p))

for i in range(N):
    y = i * d
    for j in range(N):
        x = j * d
        s = random.randint(0, 2)
        C.stroke(path.circle(x * p, y * p, 1 * p), [deco.filled([state[s]])])

C.writePDFfile('8neighbor.pdf', write_textaspath=True)


