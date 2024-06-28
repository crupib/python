from numpy import array, pi, sin, cos
from pyx import *
import os
import sys

p2 = 0.395 / 0.5

#os.environ['PATH'] =  '/Library/TeX/texbin:${PATH}'
name =  os.path.basename(sys.argv[0]).split('.')[0]

text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

C = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])

C.stroke(path.line(-10 * p2, 0 * p2, 2 * p2, 0 * p2),[deco.earrow.Large, style.linewidth.Thick])
C.stroke(path.line(0 * p2, -2 * p2, 0 * p2, 10 * p2),[deco.earrow.Large, style.linewidth.Thick])

t = pi / 2.8
#f = lambda v: 1.5 * v

f = lambda v: array([2 * v[0] * cos(t) - v[1] * sin(t),
                     v[0] * sin(t) + 3 * v[1] * cos(t)]) * 0.9


o = array([0, 0])
v = f(array([2, 1]))
w = f(array([1, 3]))
vw = v + w

fv = f(v)
fw = f(w)
fvw = f(vw)

def arrow(P, Q):
    C.stroke(path.line(P[0] * p2, P[1] * p2, Q[0] * p2, Q[1] * p2),[deco.earrow.LArge, style.linewidth.THIck])

def curve(P):
    c = path.path(path.moveto(P[0][0] * p2, P[0][1] * p2))
    for p in P[1:]:
        c.append(path.lineto(p[0] * p2, p[1] * p2))
    C.stroke(c, [style.linewidth.Thick, style.linestyle.dashed])

# Huge→huge
C.text((o[0] + 0.1) * p2, (o[1] - 0.1) * p2, r"\huge $\vv{0}_W$" ,[text.halign.left, text.valign.top])
#C.text(fv[0] * p2, fv[1] * p2, r"\huge $f(\vv{x})$" ,[text.halign.left, text.valign.bottom])
C.text((fv[0] - 0.1) * p2, (fv[1] + 0.1) * p2, r"\huge $f(\vv{x})$" ,[text.halign.left, text.valign.bottom])
C.text(fw[0] * p2, fw[1] * p2, r"\huge $f(\vv{y})$" ,[text.halign.right, text.valign.top])
C.text((fvw[0] + 0.6) * p2, (fvw[1] - 0.1) * p2, r"\huge $f(\vv{x}+\vv{y})=f(\vv{x})+f(\vv{y})$" ,[text.halign.center, text.valign.bottom])

'''
arrow(o, v)
arrow(o, w)
arrow(o, v + w)
curve([v, v + w, w])
'''    
arrow(o, fv)
arrow(o, fw)
arrow(o, fvw)
curve([fv, fvw, fw])

import warnings
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    C.writePDFfile(name + '.pdf', write_textaspath=True)

os.system('rm tmp*')
