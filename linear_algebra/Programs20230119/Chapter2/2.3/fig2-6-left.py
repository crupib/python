from numpy import array, pi, sin, cos
from pyx import *

unit.set(uscale=2, vscale=2, wscale=2, xscale=2)
text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

C = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])

C.stroke(path.line(-2, 0, 10, 0),[deco.earrow.Large, style.linewidth.Thick])
C.stroke(path.line(0, -2, 0, 10),[deco.earrow.Large, style.linewidth.Thick])

t = pi / 2.8
#f = lambda v: 1.5 * v

f = lambda v: array([2 * v[0] * cos(t) - v[1] * sin(t),
                     v[0] * sin(t) + 3 * v[1] * cos(t)]) * 0.9

o = array([0, 0])
v = array([3, 1])
w = array([2, 5])
vw = v + w

def arrow(P, Q):
    C.stroke(path.line(P[0], P[1], Q[0], Q[1]),[deco.earrow.LArge, style.linewidth.THIck])

def curve(P):
    c = path.path(path.moveto(P[0][0], P[0][1]))
    for p in P[1:]:
        c.append(path.lineto(p[0], p[1]))
    C.stroke(c, [style.linewidth.Thick, style.linestyle.dashed])

# Huge→huge
C.text((o[0] + 0.1), (o[1] - 0.1), r"\huge $\vv{0}_V$" ,[text.halign.left, text.valign.top])
C.text(v[0], v[1], r"\huge $\vv{x}$" ,[text.halign.left, text.valign.top])
C.text(w[0], w[1], r"\huge $\vv{y}$" ,[text.halign.right, text.valign.bottom])
C.text(vw[0], vw[1], r"\huge $\vv{x}+\vv{y}$" ,[text.halign.left, text.valign.bottom])

arrow(o, v)
arrow(o, w)
arrow(o, (v + w))
curve([v, (v + w), w])

C.writePDFfile('fig2-6-left.pdf')

