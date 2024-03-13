from numpy import array
from pyx import *

unit.set(uscale=2, vscale=2, wscale=2, xscale=2)
text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

c = canvas.canvas()

A = array([0, 0])
B = array([1, 3])
C = array([3, 1])
D = B + C

x = B / 2.
y = C + x

c.stroke(path.line(A[0], A[1],  B[0], B[1]), [deco.earrow.large(), style.linewidth.Thick])
c.text(x[0], x[1], r"\huge$\vec{x}$" ,[text.halign.right, text.valign.bottom])

c.stroke(path.line(C[0], C[1],  D[0], D[1]), [deco.earrow.large(), style.linewidth.Thick])
c.text(y[0], y[1], r"\huge$\vec{x}$" ,[text.halign.left, text.valign.top])

c.stroke(path.line(A[0], A[1],  C[0], C[1]), [style.linestyle.dashed])
c.stroke(path.line(B[0], B[1],  D[0], D[1]), [style.linestyle.dashed])

c.writePDFfile('fig2-1-left.pdf')

