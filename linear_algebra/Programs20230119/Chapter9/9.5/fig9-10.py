from pyx import *
from numpy import linspace

f = lambda x: x / (1 + x)
g = lambda x: min(1, x)

unit.set(uscale=4, vscale=4, wscale=4, xscale=2)
text.set(text.LatexEngine)

C = canvas.canvas()

text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')

C.stroke(path.line(-0.5, 0, 5, 0),[deco.earrow])
C.stroke(path.line(0, -0.5, 0, 2),[deco.earrow])

C.text(-0.1, -0.1, r"\huge O" ,[text.halign.right, text.valign.top])
C.text(5, -0.1, r"\huge $t$" ,[text.halign.center, text.valign.top])
C.text(-0.1, 2, r"\huge$f\left(t\right)$" ,[text.halign.right, text.valign.middle])
C.text(1, -0.1, r"\huge$1$" ,[text.halign.center, text.valign.top])
C.text(-0.1, 1, r"\huge$1$" ,[text.halign.right, text.valign.middle])

curve = path.path(path.moveto(0, 0))
for x in linspace(0, 5, 100):
    curve.append(path.lineto(x, f(x)))
C.stroke(curve, [style.linewidth.thin])

curve = path.path(path.moveto(0, 0))
for x in linspace(0, 5, 100):
    curve.append(path.lineto(x, g(x)))
C.stroke(curve, [style.linewidth.thin])

C.text(5, 0.5, r"\huge$\displaystyle\frac{t}{1+t}$", [text.halign.left, text.valign.middle])
C.text(5, 1.5, r"\huge$\min\left\{t, 1\right\}$", [text.halign.left, text.valign.middle])
C.stroke(path.line(4.95, 0.5, 4.5, (f(4.5)-0.01)),[deco.earrow])
C.stroke(path.line(4.95, 1.4, 4.5, 1.01),[deco.earrow])
C.stroke(path.line(1, 0, 1, 1),[style.linewidth.thin, style.linestyle.dashed])
C.stroke(path.line(0, 1, 1, 1),[style.linewidth.thin, style.linestyle.dashed])

C.writePDFfile('fig9-10.pdf')
