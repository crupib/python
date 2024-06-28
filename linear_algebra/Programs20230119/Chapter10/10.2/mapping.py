import two_circles
from pyx import *

C = canvas.canvas()

text.set(text.LatexEngine)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

C = canvas.canvas()

x1, y1 = 0.0, 0.0
x2, y2 = 20.0, 0.0

C.stroke(path.circle(x1, y1, 6))
C.stroke(path.circle(x1, y1, 4), [deco.filled([color.grey(0.75)])])
C.stroke(path.circle(x2, y2, 7))
C.stroke(path.circle(x2, y2, 4), [deco.filled([color.grey(0.75)])])

def line(x1, y1, r1, x2, y2, r2):
    p1, q1, p2, q2, p3, q3, p4, q4 = two_circles.f(x1, y1, r1, x2, y2, r2)
    C.stroke(path.line(p1, q1, p2, q2))
    C.stroke(path.line(p3, q3, p4, q4))

line(x1, y1, 6, x2, y2, 4)
line(x1, y1, 4, x2, y2, 4)
line(x1, y1, 4, x2, y2, 7)

C.text(x1, y1, r"\Huge$\mathrm{range}(\vv{A}^*)$", [text.halign.center, text.valign.middle])
C.text(x2, y2, r"\Huge$\mathrm{range}(\vv{A})$", [text.halign.center, text.valign.middle])

C.text(x1, 5, r"\Huge$\mathbb{K}^n$", [text.halign.center, text.valign.middle])
C.text(x2, 6, r"\Huge$\mathbb{K}^m$", [text.halign.center, text.valign.middle])

x3, y3 = -4, 4
C.stroke(path.circle(x3, y3, 0.05), [deco.filled([color.grey(0.0)])])
C.text(x3, y3 - 0.1, r"\Huge$\vv{x}$", [text.halign.right, text.valign.top])
x4, y4 = two_circles.h(x1, y1, 4, x3, y3)
C.stroke(path.line(x3, y3, x4, y4))
C.stroke(path.circle(x4, y4, 0.05), [deco.filled([color.grey(0.0)])])
C.text(x4, y4, r"\Huge$\vv{Px}$", [text.halign.left, text.valign.top])

x5, y5 = 24, 4
C.stroke(path.circle(x5, y5, 0.05), [deco.filled([color.grey(0.0)])])
C.text(x5, y5 - 0.1, r"\Huge$\vv{y}$", [text.halign.left, text.valign.top])
x6, y6 = two_circles.h(x2, y2, 4, x5, y5)
C.stroke(path.line(x5, y5, x6, y6))
C.stroke(path.circle(x6, y6, 0.05), [deco.filled([color.grey(0.0)])])
C.text(x6, y6, r"\Huge$\vv{Qy}$", [text.halign.right, text.valign.top])

C.writePDFfile('mapping.pdf')
