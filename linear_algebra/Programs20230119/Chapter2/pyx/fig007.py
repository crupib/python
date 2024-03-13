import warnings
import sys
import tangent

from pyx import *
import os

#os.environ['PATH'] = '/Library/TeX/texbin:${PATH}'

C = canvas.canvas()

text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

x1, y1 = 0.0, 0.0
x2, y2 = 15.0, 0.0

C = canvas.canvas()

C.stroke(path.circle(x1, y1, 4))
C.stroke(path.circle(x1, y1, 2), [deco.filled([color.grey(0.75)])])
C.stroke(path.circle(x2, y2, 5))
C.stroke(path.circle(x2, y2, 3), [deco.filled([color.grey(0.75)])])

p1, q1, p2, q2, p3, q3, p4, q4 = tangent.f(x1, y1, 4, x2, y2, 3)
C.stroke(path.line(p1, q1, p2, q2))
C.stroke(path.line(p3, q3, p4, q4))

p1, q1, p2, q2, p3, q3, p4, q4 = tangent.f(x1, y1, 2, x2, y2, 0)
C.stroke(path.line(p1, q1, p2, q2))
C.stroke(path.line(p3, q3, p4, q4))

C.text(0, 3, r"\Huge$V$", [text.halign.center, text.valign.middle])
C.text(15, 4, r"\Huge$W$", [text.halign.center, text.valign.middle])
C.text(7.5, 4, r"\Huge$\vv{f}$", [text.halign.center, text.valign.middle])
C.text(0, 1, r"\huge$\mathrm{kernel}(\vv{f})$",
       [text.halign.center, text.valign.middle])
C.text(15, 2, r"\huge$\mathrm{range}(\vv{f})$",
       [text.halign.center, text.valign.middle])
C.text(p2 + 0.1, q2, r"\huge$\vv{0}_W$",
       [text.halign.left, text.valign.middle])


'''
x3, y3, x4, y4, x5, y5, x6, y6 = tangent.g(x1, y1, r1, x2, y2, r2)
C.stroke(path.line(x3, y3, x4, y4))
C.stroke(path.line(x5, y5, x6, y6))
'''

name = os.path.basename(sys.argv[0]).split('.')[0]

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    C.writePDFfile(name + '.pdf')

os.system('rm tmp*.*')
