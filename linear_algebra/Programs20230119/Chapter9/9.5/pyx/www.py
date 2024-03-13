from numpy import *
from pyx import *

p = 0.495 / 0.5

C = canvas.canvas([trafo.scale(sx=1, sy=1)])
text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath, amsfonts, amssymb}')

#latex = text.texrunner(mode="latex")
#latex.preamble(r'\usepackage{amsmath}')
#latex.preamble(r'\usepackage{amsfonts}')
#latex.preamble(r'\usepackage{amssymb}')

N = 3
d = 3
state = [color.grey.white, color.grey.black]

for i in range(N):
    y = i * d
    C.stroke(path.line(0 * p, y * p, (N - 1) * d * p, y * p))
    for j in range(N):
        x = j * d
        C.stroke(path.line(x * p, 0 * p, x * p, (N  - 1) * d * p))

for i in range(N - 1):
    y0 = i * d
    y1 = (i + 1) * d
    C.stroke(path.line(0 * p, y * p, (N - 1) * d * p, y * p))
    for j in range(N - 1):
        x0 = j * d
        x1 = (j + 1) * d
        C.stroke(path.line(x0 * p, y0 * p, x1 * p, y1 * p))
        C.stroke(path.line(x0 * p, y1 * p, x1 * p, y0 * p))

for i in range(N):
    y = i * d
    for j in range(N):
        x = j * d
        s = random.randint(0, 2)
        C.stroke(path.circle(x * p, y * p, 0.67 * p), [deco.filled([color.grey.white])])

C.text(d * p, d * p, r"\huge $a$" ,[text.halign.center, text.valign.middle])

C.text(0 * p, 0 * p, r"\huge sw" ,[text.halign.center, text.valign.middle])
C.text(d * p, 0 * p, r"\huge s" ,[text.halign.center, text.valign.middle])
C.text(2 * d * p, 0 * p, r"\huge se" ,[text.halign.center, text.valign.middle])

C.text(0 * p, d * p, r"\huge w" ,[text.halign.center, text.valign.middle])
C.text(2 * d * p, d * p, r"\huge e" ,[text.halign.center, text.valign.middle])

C.text(0 * p, 2 * d * p, r"\huge nw" ,[text.halign.center, text.valign.middle])
C.text(d * p, 2 * d * p, r"\huge n" ,[text.halign.center, text.valign.middle])
C.text(2 * d * p, 2 * d * p, r"\huge ne" ,[text.halign.center, text.valign.middle])


C.writePDFfile('www.pdf', write_textaspath=True)

