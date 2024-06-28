from numpy import *
from pyx import *

unit.set(uscale=1, vscale=1, wscale=1, xscale=2)
C = canvas.canvas()

text.set(text.LatexEngine)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')

f = lambda t: array([(18 * cos(t) + 10), (4 * sin(t))])
t0 = arccos(-8.5 / 18)
t1 = 2 * pi - t0

elps0 = path.path(path.moveto(*f(pi / 2)))
for t in linspace(pi / 2, t0):
    elps0.append(path.lineto(*f(t)))
for t in linspace(t1, 3 * pi / 2, 100):
    elps0.append(path.lineto(*f(t)))
C.stroke(elps0, [deco.filled([color.gray(0.9)])])

elps1 = path.path(path.moveto(*f(t0)))
for t in linspace(t0, t1):
    elps1.append(path.lineto(*f(t)))
C.stroke(elps1, [deco.filled([color.gray(0.7)])])

rect1 = path.path(path.moveto(-10, -6),
                  path.lineto(10, -6),
                  path.lineto(10, 10),
                  path.lineto(-10, 10), 
                  path.closepath())
C.stroke(rect1)

rect2 = path.path(path.moveto(1.5, -6),
                  path.lineto(1.5, 6),
                  path.lineto(-10, 6))
C.stroke(rect2)

rect3 = path.path(path.moveto(4.5, -6),
                  path.lineto(4.5, 8),
                  path.lineto(-10, 8))
C.stroke(rect3)

C.text(-4, 5, r'\huge $Y$' ,[text.halign.center, text.valign.middle])
C.text(-4, 7, r'\huge $\partial Y$' ,[text.halign.center, text.valign.middle])
C.text(-4, 9, r'\huge $\left(Y\cup\partial Y\right)^c$' ,[text.halign.center, text.valign.middle])


C.text(-1, -2, r"\huge $A'$",[text.halign.center, text.valign.middle])
C.text(7, 3, r'\huge $B$' ,[text.halign.center, text.valign.middle])

C.stroke(path.circle(-4, 0, 1), [deco.filled([color.gray.black])])
C.text(-4, 0, r'\huge $S_1$' ,[color.gray.white, text.halign.center, text.valign.middle])
C.stroke(path.circle(1.5, 2, 1), [deco.filled([color.gray.black])])
C.text(1.5, 2, r'\huge $S_2$' ,[color.gray.white, text.halign.center, text.valign.middle])
C.stroke(path.circle(3, 0, 1), [deco.filled([color.gray.black])])
C.text(3, 0, r'\huge $S_3$' ,[color.gray.white, text.halign.center, text.valign.middle])
C.stroke(path.circle(4.5, -2, 1), [deco.filled([color.gray.black])])
C.text(4.5, -2, r'\huge $S_4$' ,[color.gray.white, text.halign.center, text.valign.middle])
C.stroke(path.circle(7, 0, 1), [deco.filled([color.gray.black])])
C.text(7, 0, r'\huge $S_5$' ,[color.gray.white, text.halign.center, text.valign.middle])


C.writePDFfile('fig9-11.pdf')

