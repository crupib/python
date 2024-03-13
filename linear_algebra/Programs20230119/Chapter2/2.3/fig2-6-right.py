from numpy import array, pi, sin, cos
from pyx import *

unit.set(uscale=2, vscale=2, wscale=2, xscale=2)
text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

C = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])

C.stroke(path.line(-10, 0, 2, 0),[deco.earrow.Large, style.linewidth.Thick])
C.stroke(path.line(0, -2, 0, 10),[deco.earrow.Large, style.linewidth.Thick])

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
    C.stroke(path.line(P[0], P[1], Q[0], Q[1]),[deco.earrow.LArge, style.linewidth.THIck])

def curve(P):
    c = path.path(path.moveto(P[0][0], P[0][1]))
    for p in P[1:]:
        c.append(path.lineto(p[0], p[1]))
    C.stroke(c, [style.linewidth.Thick, style.linestyle.dashed])

# Huge→huge
C.text((o[0] + 0.1), (o[1] - 0.1), r"\huge $\vv{0}_W$" ,[text.halign.left, text.valign.top])
#C.text(fv[0], fv[1], r"\huge $f(\vv{x})$" ,[text.halign.left, text.valign.bottom])
C.text((fv[0] - 0.1), (fv[1] + 0.1), r"\huge $f(\vv{x})$" ,[text.halign.left, text.valign.bottom])
C.text(fw[0], fw[1], r"\huge $f(\vv{y})$" ,[text.halign.right, text.valign.top])
C.text((fvw[0] + 0.6), (fvw[1] - 0.1), r"\huge $f(\vv{x}+\vv{y})=f(\vv{x})+f(\vv{y})$" ,[text.halign.center, text.valign.bottom])

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

C.writePDFfile('fig2-6-right.pdf')

