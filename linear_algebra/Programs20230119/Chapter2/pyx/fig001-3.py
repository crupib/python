from numpy import array
from pyx import *
import os
import sys


os.environ['PATH'] =  '/Library/TeX/texbin:${PATH}'
name =  os.path.basename(sys.argv[0]).split('.')[0]

text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

c = canvas.canvas()


A = array([0, 0])
B = array([1, 3])
C = array([4, 4])
D = C - B

x = D + B / 2.
y = D / 2.
z = C / 2.

c.stroke(path.line(D[0], D[1],  C[0], C[1]), [deco.earrow.large(), style.linewidth.Thick])
c.text(x[0], x[1], r"\Large $\vec{x}$" ,[text.halign.left, text.valign.top])

c.stroke(path.line(A[0], A[1],  D[0], D[1]), [deco.earrow.large(), style.linewidth.Thick])
c.text(y[0], y[1], r"\Large $\vec{y}$" ,[text.halign.left, text.valign.top])

c.stroke(path.line(A[0] - 0.1, A[1] + 0.1,  C[0] - 0.1, C[1] + 0.1), [deco.earrow.large(), style.linewidth.Thick])
c.text(z[0] - 0.1, z[1] + 0.1, r"\Large $\vec{y}+\vec{x}$" ,[text.halign.right, text.valign.bottom])

c.stroke(path.line(A[0], A[1],  C[0], C[1]), [style.linestyle.dashed])

import warnings
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    c.writePDFfile(name + '.pdf')

os.system('rm tmp*')
