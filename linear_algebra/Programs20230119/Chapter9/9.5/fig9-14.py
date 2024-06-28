from numpy import *
from pyx import *

unit.set(uscale=1, vscale=1, wscale=1, xscale=1)
C = canvas.canvas()
text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath, amsfonts, amssymb}')

N = 3
d = 3
state = [color.grey.white, color.grey.black]

for i in range(N):
    y = i * d
    C.stroke(path.line(0, y, (N - 1) * d, y))
    for j in range(N):
        x = j * d
        C.stroke(path.line(x, 0, x, (N  - 1) * d))

for i in range(N - 1):
    y0 = i * d
    y1 = (i + 1) * d
    C.stroke(path.line(0, y, (N - 1) * d, y))
    for j in range(N - 1):
        x0 = j * d
        x1 = (j + 1) * d
        C.stroke(path.line(x0, y0, x1, y1))
        C.stroke(path.line(x0, y1, x1, y0))

for i in range(N):
    y = i * d
    for j in range(N):
        x = j * d
        s = random.randint(0, 2)
        C.stroke(path.circle(x, y, 0.67), [deco.filled([color.grey.white])])

C.text(d, d, r"\huge $a$" ,[text.halign.center, text.valign.middle])

C.text(0, 0, r"\huge sw" ,[text.halign.center, text.valign.middle])
C.text(d, 0, r"\huge s" ,[text.halign.center, text.valign.middle])
C.text(2 * d, 0, r"\huge se" ,[text.halign.center, text.valign.middle])

C.text(0, d, r"\huge w" ,[text.halign.center, text.valign.middle])
C.text(2 * d, d, r"\huge e" ,[text.halign.center, text.valign.middle])

C.text(0, 2 * d, r"\huge nw" ,[text.halign.center, text.valign.middle])
C.text(d, 2 * d, r"\huge n" ,[text.halign.center, text.valign.middle])
C.text(2 * d, 2 * d, r"\huge ne" ,[text.halign.center, text.valign.middle])


C.writePDFfile('fig9-14.pdf')

