from pyx import *

def mycanvas(u=5, v=2.5, w=2.5, x=2.5, latex=False):
    unit.set(uscale=u, vscale=v, wscale=v, xscale=x)
    if latex:
        text.set(text.LatexRunner)
        text.preamble(r'\usepackage{amsmath, amsfonts,amssymb}') 
        text.preamble(r'\newcommand{\vv}[1]{\boldsymbol{#1}}')
        text.preamble(r'\newcommand{\inner}[2]{\left\langle{#1}\bigm|{#2}\right\rangle}')
        text.preamble(r'\newcommand{\norm}[1]{\left\|{#1}\right\|}')
    return canvas.canvas()

def make_polygon(P, closed=True):
    curve = path.path(path.moveto(*P[0]))
    for p in P[1:]:
        curve.append(path.lineto(*p))
    if closed:
        curve.append(path.closepath())
    return curve

if __name__=='__main__':
    from numpy import *

    C = mycanvas(x=1, latex=True)
    T1 = trafo.scale(sx=sqrt(2), sy=1)
    T2 = trafo.rotate(45)
    P = [(cos(t), sin(t)) for t in linspace(0, 2*pi, 6)]
    C.stroke(make_polygon(P), [T1, T2, deco.filled([color.grey(0.8)])])
    C.stroke(path.circle(0, 0, 1), [T2*T1])
    C.stroke(path.line(-1.5, 0, 1.5, 0), [deco.earrow()])
    C.stroke(path.line(0, -1.5, 0, 1.5), [deco.earrow()])
    s = r'''
        $\boldsymbol{T}_2=\left[\begin{array}{rr}
        \cos 45^\circ&-\sin 45^\circ\\
        \sin 45^\circ&\cos 45^\circ\\
        \end{array}\right]$
        '''
    C.text(0.25, 0, s, [trafo.rotate(45, x=-0.25, y=0)])
    C.writePDFfile('mypyx.pdf')
    
