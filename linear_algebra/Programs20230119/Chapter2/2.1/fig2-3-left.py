from pyx import *

unit.set(uscale=2, vscale=2, wscale=2, xscale=1)
text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

c = canvas.canvas()

c.stroke(path.line( 0, 1,  6, 1), [deco.earrow()])
c.stroke(path.line( 1, 0,  1, 6), [deco.earrow()])

c.stroke(path.circle(4, 3,  0.025), [deco.filled([color.grey(0.)])])

c.stroke(path.line( 1, 1,  4, 3), [deco.earrow.Large ,style.linewidth.THIck])

c.stroke(path.line( 4, 1,  4, 3), [style.linestyle.dashed])
c.stroke(path.line( 1, 3,  4, 3), [style.linestyle.dashed])

c.text(0.9, 0.9, r"\huge O" ,[text.halign.boxright, text.valign.top])
#c.text(4, 1, r"\huge$x_1$" ,[text.halign.boxcenter, text.valign.top])
c.text(4, 0.9, r"\huge$x_1$" ,[text.halign.boxcenter, text.valign.top])
#c.text(1, 3, r"\huge$x_2$" ,[text.halign.boxright, text.valign.middle])
c.text(0.9, 3, r"\huge$x_2$" ,[text.halign.boxright, text.valign.middle])

c.text(4, 3, r"\huge$\left(x_1,x_2\right)$" ,[text.halign.boxleft, text.valign.bottom])

c.writePDFfile('fig2-3-left.pdf')

