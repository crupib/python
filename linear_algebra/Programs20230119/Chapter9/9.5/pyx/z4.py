from numpy import *
from pyx import *

p = 0.068 / 0.5
C = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])

N = 10
d = 5
state = [color.grey.white, color.grey.black]

C.stroke(path.line(0 * p, 0 * p, d * p, 0 * p))
C.stroke(path.line(d * p, 0 * p, d * p, d * p))
C.stroke(path.line(d * p, d * p, 0 * p, d * p))
C.stroke(path.line(0 * p, d * p, 0 * p, 0 * p))
C.stroke(path.line(0 * p, d * p, d * p, 0 * p))
C.stroke(path.line(0 * p, 0 * p, d * p, d * p))
C.stroke(path.circle(0 * p, 0 * p, 1 * p), [deco.filled([state[1]])])
C.stroke(path.circle(0 * p, d * p, 1 * p), [deco.filled([state[1]])])
C.stroke(path.circle(d * p, 0 * p, 1 * p), [deco.filled([state[1]])])
C.stroke(path.circle(d * p, d * p, 1 * p), [deco.filled([state[1]])])

C.writePDFfile('z4.pdf', write_textaspath=True)


