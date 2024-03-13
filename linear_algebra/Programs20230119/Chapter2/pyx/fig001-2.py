from numpy import array
from pyx import *
import os
import sys

p = 0.798 / 0.5

#os.environ['PATH'] =  '/Library/TeX/texbin:${PATH}'
name =  os.path.basename(sys.argv[0]).split('.')[0]

text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

c = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])


A = array([0, 0])
B = array([1, 3])
C = array([4, 4])
x = A + (B - A) / 2.
y = B + (C - B) / 2.
z = A + (C - A) / 2.

c.stroke(path.line(A[0] * p, A[1] * p,  B[0] * p, B[1] * p), [deco.earrow.large(), style.linewidth.Thick])
c.text(x[0] * p, x[1] * p, r"\huge$\vec{x}$" ,[text.halign.right, text.valign.bottom])

c.stroke(path.line(B[0] * p, B[1] * p,  C[0] * p, C[1] * p), [deco.earrow.large(), style.linewidth.Thick])
c.text(y[0] * p, y[1] * p, r"\huge$\vec{y}$" ,[text.halign.right, text.valign.bottom])

c.stroke(path.line((A[0] + 0.1) * p, (A[1] - 0.1) * p,  (C[0] + 0.1) * p, (C[1] - 0.1) * p), [deco.earrow.large(), style.linewidth.Thick])
c.text((z[0] + 0.1) * p, (z[1] - 0.1) * p, r"\huge$\vec{x}+\vec{y}$" ,[text.halign.left, text.valign.top])

c.stroke(path.line(A[0] * p, A[1] * p,  C[0] * p, C[1] * p), [style.linestyle.dashed])

import warnings
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    c.writePDFfile(name + '.pdf', write_textaspath=True)

os.system('rm tmp*')
