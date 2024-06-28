from numpy import *
from mypyx import *
import two_circles

C = mycanvas(x=2.5, latex=True)

N = 1
for n in range(N):
    x = n * (N * 3)
    y = 0
    for r in range(N, 0, -1):
        if r == N - n:
            Deco = [deco.filled([color.cmyk.Grey])]
        else:
            Deco = [deco.filled([color.grey.white])]
        C.stroke(path.circle(x, y, r), Deco)

C.stroke(path.circle(N * (N * 3), 0, 0.1), [deco.filled([color.grey.black])])
C.text((N * (N * 3) + 0.2), 0, r"\huge$\mathbf{0}$", [text.halign.left, text.valign.middle])

C.text(0, N, r"\LARGE$K_1=K_1^{(1)}$", [text.halign.center, text.valign.bottom])
    
for n in range(N):
    x1, y1, r1 = n * (N * 3), 0, N - n
    x2, y2, r2 = (n + 1) * (N * 3), 0, N - n - 1
    x3, y3, x4, y4, x5, y5, x6, y6 = two_circles.f(x1, y1, r1, x2, y2, r2)
    C.stroke(path.line(x3, y3, x4, y4))
    C.stroke(path.line(x5, y5, x6, y6))

    C.text(0, 0.5, r"\LARGE$\boldsymbol{v}_0$", [text.halign.center, text.valign.middle])

    C.writePDFfile('circle1.pdf')
