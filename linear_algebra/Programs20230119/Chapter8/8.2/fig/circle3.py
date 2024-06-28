from numpy import *
from mypyx import *
import two_circles

C = mycanvas(x=2.5, latex=True)

N = 3
    
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
    
for n in range(N):
    x1, y1, r1 = n * (N * 3), 0, N - n
    x2, y2, r2 = (n + 1) * (N * 3), 0, N - n - 1
    x3, y3, x4, y4, x5, y5, x6, y6 = circle.f(x1, y1, r1, x2, y2, r2)
    C.stroke(path.line(x3, y3, x4, y4))
    C.stroke(path.line(x5, y5, x6, y6))

for n in range(N - 1):
    x1, y1, r1 = n * (N * 3), 0, N - n - 1
    x2, y2, r2 = (n + 1) * (N * 3), 0, N - n - 2
    x3, y3, x4, y4, x5, y5, x6, y6 = two_circles.f(x1, y1, r1, x2, y2, r2)
    C.stroke(path.line(x3, y3, x4, y4))
    C.stroke(path.line(x5, y5, x6, y6))

for n in range(N - 2):
    x1, y1, r1 = n * (N * 3), 0, N - n - 2
    x2, y2, r2 = (n + 1) * (N * 3), 0, N - n - 3
    x3, y3, x4, y4, x5, y5, x6, y6 = circle.f(x1, y1, r1, x2, y2, r2)
    C.stroke(path.line(x3, y3, x4, y4))
    C.stroke(path.line(x5, y5, x6, y6))

C.text(0, 2.5, r"\huge$\boldsymbol{v}_5$", [text.halign.right, text.valign.middle])
C.text(N * 3, 1.5, r"\huge$\boldsymbol{v}_6$", [text.halign.center, text.valign.middle])
C.text(2 * N * 3, 0.5, r"\huge$\boldsymbol{v}_7$", [text.halign.left, text.valign.middle])
C.stroke(path.line(0.1, 2.5, (N * 3 - 0.5), 1.5), [deco.earrow.large, style.linewidth.THIck])
C.stroke(path.line((N * 3 + 0.5), 1.5, 2 * N * 3 - 0.1, 0.5), [deco.earrow.large, style.linewidth.THIck])

C.text(N * 3, -1.5, r"\huge$\boldsymbol{v}_8$", [text.halign.center, text.valign.middle])
C.text(2 * N * 3, -0.5, r"\huge$\boldsymbol{v}_9$", [text.halign.left, text.valign.middle])
C.stroke(path.line((N * 3 + 0.5), -1.5, 2 * N * 3 - 0.1, -0.5), [deco.earrow.large, style.linewidth.THIck])


C.text(0, N, r"\huge$K_3=K_3^{(3)}$", [text.halign.center, text.valign.bottom])
C.text(N * 3, (N - 1 + 0.04), r"\huge$K_3^{(2)}$", [text.halign.center, text.valign.bottom])
C.text(2 * N * 3, (N - 2 + 0.04), r"\huge$K_3^{(1)}$", [text.halign.center, text.valign.bottom])

C.writePDFfile('circle3.pdf')
