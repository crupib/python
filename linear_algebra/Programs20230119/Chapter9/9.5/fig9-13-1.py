from numpy import *
from pyx import *

unit.set(uscale=0.2, vscale=0.2, wscale=1, xscale=0.2)
C = canvas.canvas()

N = 10
d = 5
state = [color.grey.white, color.grey.black]

C.stroke(path.circle(0, 0, 1), [deco.filled([state[1]])])

C.writePDFfile('fig9-13-1.pdf')


