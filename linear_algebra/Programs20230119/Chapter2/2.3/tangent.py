from numpy import *


def f(x1, y1, r1, x2, y2, r2):
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

    return x3, y3, x4, y4, x5, y5, x6, y6


def g(x1, y1, r1, x2, y2, r2):
    s = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    sa = (r2 + r1) / s
    ca1 = sqrt(s ** 2 - (r2 + r1) ** 2) / s
    ca2 = - ca1

    cb = (x2 - x1) / s
    sb = (y2 - y1) / s

    ct1 = cb * ca1 + sb * sa
    st1 = sb * ca1 - cb * sa

    ct2 = cb * ca2 + sb * sa
    st2 = sb * ca2 - cb * sa

    x3 = x1 - r1 * st1
    y3 = y1 + r1 * ct1
    x4 = x2 + r2 * st1
    y4 = y2 - r2 * ct1

    x5 = x1 - r1 * st2
    y5 = y1 + r1 * ct2
    x6 = x2 + r2 * st2
    y6 = y2 - r2 * ct2

    return x3, y3, x4, y4, x5, y5, x6, y6


if __name__ == '__main__':
    from pyx import *

    C = canvas.canvas()

    text.set(text.LatexRunner)
    text.preamble(r'\usepackage{amsmath}')
    text.preamble(r'\usepackage{amsfonts}')
    text.preamble(r'\usepackage{amssymb}')
    text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

    x1, y1, r1 = 1.0, 2.0, 1.0
    x2, y2, r2 = 4.0, 6.0, 2.0

    C = canvas.canvas()

    C.stroke(path.circle(x1, y1, r1), [deco.filled([color.cmyk.Yellow])])
    C.stroke(path.circle(x2, y2, r2), [deco.filled([color.cmyk.Cyan])])

    x3, y3, x4, y4, x5, y5, x6, y6 = f(x1, y1, r1, x2, y2, r2)
    C.stroke(path.line(x3, y3, x4, y4))
    C.stroke(path.line(x5, y5, x6, y6))

    x3, y3, x4, y4, x5, y5, x6, y6 = g(x1, y1, r1, x2, y2, r2)
    C.stroke(path.line(x3, y3, x4, y4))
    C.stroke(path.line(x5, y5, x6, y6))


    C.writePDFfile('tangent.pdf')

