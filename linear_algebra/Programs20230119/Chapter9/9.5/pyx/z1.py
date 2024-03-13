from numpy import *
from pyx import *

p = 0.068 / 0.5
C = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])

N = 10
d = 5
state = [color.grey.white, color.grey.black]

C.stroke(path.circle(0 * p, 0 * p, 1 * p), [deco.filled([state[1]])])

C.writePDFfile('z1.pdf', write_textaspath=True)


