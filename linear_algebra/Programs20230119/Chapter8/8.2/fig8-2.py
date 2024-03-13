from numpy import *

def f(a, b):
    x1, y1, r1 = a
    x2, y2, r2 = b
    s = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    sa = (r2 - r1) / s
    ca1 = sqrt(s ** 2 - (r2 - r1) ** 2) / s
    ca2 = - ca1

    cb = (x2 - x1) / s
    sb = (y2 - y1) / s

    ct1 = cb * ca1 + sb * sa
    st1 = sb * ca1 - cb * sa

    ct2 = cb * ca2 + sb * sa
    st2 = sb * ca2 - cb * sa

    x3 = x1 + r1 * st1
    y3 = y1 - r1 * ct1
    x4 = x2 + r2 * st1
    y4 = y2 - r2 * ct1

    x5 = x1 + r1 * st2
    y5 = y1 - r1 * ct2
    x6 = x2 + r2 * st2
    y6 = y2 - r2 * ct2

    return (x3, y3, x4, y4), (x5, y5, x6, y6)



if __name__ == '__main__':
    from pyx import *

    unit.set(uscale=3, vscale=3, wscale=3, xscale=2)
    text.set(text.LatexRunner)
    text.preamble(r'\usepackage{amsmath}')
    text.preamble(r'\usepackage{amsfonts}')
    text.preamble(r'\usepackage{amssymb}')

    C = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])

    N = 2
    
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
    
    C.text(0, N, r"\huge$K_2=K_2^{(2)}$", [text.halign.center, text.valign.bottom])
    C.text(N * 3, (N - 1 + 0.04), r"\huge$K_2^{(1)}$", [text.halign.center, text.valign.bottom])
    
    for n in range(N):
        a = n * (N * 3), 0, N - n
        b = (n + 1) * (N * 3), 0, N - n - 1
        c, d = f(a, b)
        C.stroke(path.line(*c))
        C.stroke(path.line(*d))

    for n in range(N - 1):
        a = n * (N * 3), 0, N - n - 1
        b = (n + 1) * (N * 3), 0, N - n - 2
        c, d = f(a, b)
        C.stroke(path.line(*c))
        C.stroke(path.line(*d))


    C.text(0, 1.5, r"\huge$\boldsymbol{v}_1$", [text.halign.right, text.valign.middle])
    C.text(N * 3, 0.5, r"\huge$\boldsymbol{v}_2$", [text.halign.left, text.valign.middle])
    C.stroke(path.line(0.1, 1.5, N * 3 - 0.1, 0.5), [deco.earrow, style.linewidth.THick])

    C.text(0, -1.5, r"\huge$\boldsymbol{v}_3$", [text.halign.right, text.valign.middle])
    C.text(N * 3, -0.5, r"\huge$\boldsymbol{v}_4$", [text.halign.left, text.valign.middle])
    C.stroke(path.line(0.1, -1.5, N * 3 - 0.1, -0.5), [deco.earrow, style.linewidth.THick])

    C.writePDFfile('fig8-2.pdf')
