from pyx import *

unit.set(uscale=2, vscale=2, wscale=2, xscale=1)
text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

c = canvas.canvas()

c.stroke(path.line( 0, 0,  6, 0), [deco.earrow()])
c.stroke(path.line( 0, 0,  0, 6), [deco.earrow()])
c.text(0, 0, r"\huge O" ,[text.halign.right, text.valign.top])

c.text(1, -0.1, r"\huge$1$" ,[text.halign.center, text.valign.top])
c.text(0, 3, r"\huge$x_1$" ,[text.halign.right, text.valign.top])
c.stroke(path.line(1, 0,  1, 3), [style.linewidth.THICK])
c.stroke(path.line(1, 3,  0, 3), [style.linestyle.dashed])

c.text(2, -0.1, r"\huge$2$" ,[text.halign.center, text.valign.top])
c.text(0, 4, r"\huge$x_2$" ,[text.halign.right, text.valign.middle])
c.stroke(path.line(2, 0,  2, 4), [style.linewidth.THICK])
c.stroke(path.line(2, 4,  0, 4), [style.linestyle.dashed])

c.text(5, -0.1, r"\huge$n$" ,[text.halign.center, text.valign.top])
c.text(0, 2, r"\huge$x_n$" ,[text.halign.right, text.valign.middle])
c.stroke(path.line(5, 0,  5, 2), [style.linewidth.THICK])
c.stroke(path.line(5, 2,  0, 2), [style.linestyle.dashed])

c.stroke(path.line(3, 0, 3, 5), [style.linewidth.THICK])
c.stroke(path.line(4, 0, 4, 3.5), [style.linewidth.THICK])

c.writePDFfile('fig2-3-right.pdf')
