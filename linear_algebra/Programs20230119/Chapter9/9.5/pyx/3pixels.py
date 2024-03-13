from numpy import *
from pyx import *

p = 0.45 / 0.5

C = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])
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
    C.stroke(path.line(x0 * p, 0 * p, (x0 + 2 * d) * p, 0 * p))
    C.text((x0 + d) * p, 1 * p, A[n] ,[text.halign.center, text.valign.bottom])
    for i in range(3):
        x1 = x0 + i * d
        col = state[a[n][i]]
        C.stroke(path.circle(x1 * p, 0 * p, 0.25 * p), [deco.filled([col])])
        C.text(x1 * p, -0.6 * p, r'\huge $x_' + str(i + 1) + '$' ,[text.halign.center, text.valign.top])


C.writePDFfile('3pixels.pdf', write_textaspath=True)

