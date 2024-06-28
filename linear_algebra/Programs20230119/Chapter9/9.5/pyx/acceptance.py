from pyx import *
from numpy import linspace

f = lambda x: x / (1 + x)
g = lambda x: min(1, x)

p = 1.29 / 0.5
text.set(text.LatexEngine)

C = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])

text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')

C.stroke(path.line(-0.5 * p, 0 * p, 5 * p, 0 * p),[deco.earrow])
C.stroke(path.line(0 * p, -0.5 * p, 0 * p, 2 * p),[deco.earrow])

C.text(-0.1 * p, -0.1 * p, r"\huge O" ,[text.halign.right, text.valign.top])
C.text(5 * p, -0.1 * p, r"\huge $t$" ,[text.halign.center, text.valign.top])
C.text(-0.1 * p, 2 * p, r"\huge$f\left(t\right)$" ,[text.halign.right, text.valign.middle])
C.text(1 * p, -0.1 * p, r"\huge$1$" ,[text.halign.center, text.valign.top])
C.text(-0.1 * p, 1 * p, r"\huge$1$" ,[text.halign.right, text.valign.middle])

curve = path.path(path.moveto(0 * p, 0 * p))
for x in linspace(0, 5, 100):
    curve.append(path.lineto(x * p, f(x) * p))
C.stroke(curve, [style.linewidth.thin])

curve = path.path(path.moveto(0 * p, 0 * p))
for x in linspace(0, 5, 100):
    curve.append(path.lineto(x * p, g(x) * p))
C.stroke(curve, [style.linewidth.thin])

C.text(5 * p, 0.5 * p, r"\huge$\displaystyle\frac{t}{1+t}$", [text.halign.left, text.valign.middle])
C.text(5 * p, 1.5 * p, r"\huge$\min\left\{t, 1\right\}$", [text.halign.left, text.valign.middle])
C.stroke(path.line(4.95 * p, 0.5 * p, 4.5 * p, (f(4.5)-0.01) * p),[deco.earrow])
C.stroke(path.line(4.95 * p, 1.4 * p, 4.5 * p, 1.01 * p),[deco.earrow])
C.stroke(path.line(1 * p, 0 * p, 1 * p, 1 * p),[style.linewidth.thin, style.linestyle.dashed])
C.stroke(path.line(0 * p, 1 * p, 1 * p, 1 * p),[style.linewidth.thin, style.linestyle.dashed])

C.writePDFfile('fig.pdf', write_textaspath=True)
