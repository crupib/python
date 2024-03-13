from numpy import *
from pyx import *

p = 0.298 / 0.5

C = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])

text.set(text.LatexEngine)
#latex = text.texrunner(mode="latex")
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')

#u = 0.6
u = p

f = lambda t: array([(18 * cos(t) + 10), (4 * sin(t))]) * u
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

rect1 = path.path(path.moveto(-10 * u, -6 * u),
                  path.lineto(10 * u, -6 * u),
                  path.lineto(10 * u, 10 * u),
                  path.lineto(-10 * u, 10 * u), 
                  path.closepath())
C.stroke(rect1)

rect2 = path.path(path.moveto(1.5 * u, -6 * u),
                  path.lineto(1.5 * u, 6 * u),
                  path.lineto(-10 * u, 6 * u))
C.stroke(rect2)

rect3 = path.path(path.moveto(4.5 * u, -6 * u),
                  path.lineto(4.5 * u, 8 * u),
                  path.lineto(-10 * u, 8 * u))
C.stroke(rect3)

C.text(-4 * u, 5 * u, r'\huge $Y$' ,[text.halign.center, text.valign.middle])
C.text(-4 * u, 7 * u, r'\huge $\partial Y$' ,[text.halign.center, text.valign.middle])
C.text(-4 * u, 9 * u, r'\huge $\left(Y\cup\partial Y\right)^c$' ,[text.halign.center, text.valign.middle])


C.text(-1 * u, -2 * u, r"\huge $A'$",[text.halign.center, text.valign.middle])
C.text(7 * u, 3 * u, r'\huge $B$' ,[text.halign.center, text.valign.middle])

C.stroke(path.circle(-4 * u, 0, u), [deco.filled([color.gray.black])])
C.text(-4 * u, 0, r'\huge $S_1$' ,[color.gray.white, text.halign.center, text.valign.middle])
C.stroke(path.circle(1.5 * u, 2 * u, u), [deco.filled([color.gray.black])])
C.text(1.5 * u, 2 * u, r'\huge $S_2$' ,[color.gray.white, text.halign.center, text.valign.middle])
C.stroke(path.circle(3 * u, 0, u), [deco.filled([color.gray.black])])
C.text(3 * u, 0, r'\huge $S_3$' ,[color.gray.white, text.halign.center, text.valign.middle])
C.stroke(path.circle(4.5 * u, -2 * u, u), [deco.filled([color.gray.black])])
C.text(4.5 * u, -2 * u, r'\huge $S_4$' ,[color.gray.white, text.halign.center, text.valign.middle])
C.stroke(path.circle(7 * u, 0, u), [deco.filled([color.gray.black])])
C.text(7 * u, 0, r'\huge $S_5$' ,[color.gray.white, text.halign.center, text.valign.middle])


C.writePDFfile('bbb.pdf', write_textaspath=True)

