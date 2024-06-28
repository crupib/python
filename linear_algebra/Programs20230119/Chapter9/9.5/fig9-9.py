from numpy import *
from pyx import *

unit.set(uscale=0.2, vscale=0.2, wscale=0.2, xscale=0.2)
C = canvas.canvas()
text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath, amsfonts, amssymb}')

d = 1.0
state = [color.grey.white, color.grey.black]
a = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1),
     (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]

A = [r'\huge $\emptyset$',
     r'\huge $\left\{x_1\right\}$',
     r'\huge $\left\{x_2\right\}$',
     r'\huge $\left\{x_3\right\}$',
     r'\huge $\left\{x_1,\ x_2\right\}$',
     r'\huge $\left\{x_1,\ x_3\right\}$',
     r'\huge $\left\{x_2,\ x_3\right\}$', r'\Huge $X$']

for n in range(8):
    x0 = 4 * d * n
    C.stroke(path.line(x0, 0, (x0 + 2 * d), 0))
    C.text((x0 + d), 1, A[n] ,[text.halign.center, text.valign.bottom])
    for i in range(3):
        x1 = x0 + i * d
        col = state[a[n][i]]
        C.stroke(path.circle(x1, 0, 0.25), [deco.filled([col])])
        C.text(x1, -0.6, r'\huge $x_' + str(i + 1) + '$' ,[text.halign.center, text.valign.top])


C.writePDFfile('3pixels.pdf')

