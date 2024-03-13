from pyx import *

unit.set(uscale=2, vscale=2, wscale=2, xscale=1)
text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

c = canvas.canvas()

c.text(3.9, 2.9, r"\huge O" ,[text.halign.boxleft, text.valign.top])

c.stroke(path.line( 2, 1.5,  5, 1.5), [style.linestyle.dashed])
c.text(2, 1.5, r"\huge$x_1$" ,[text.halign.boxright, text.valign.bottom])

c.stroke(path.line( 5, 1.5,  7, 3), [style.linestyle.dashed])
#c.text(7, 3, r"\huge$x_2$" ,[text.halign.boxleft, text.valign.top])
c.text(7, 2.9, r"\huge$x_2$" ,[text.halign.boxleft, text.valign.top])

c.stroke(path.line( 4, 6,  7, 6), [style.linestyle.dashed])
#c.text(4, 6, r"\huge$x_3$" ,[text.halign.boxright, text.valign.middle])
c.text(4, 6.2, r"\huge$x_3$" ,[text.halign.boxright, text.valign.middle])

c.stroke(path.line( 7, 6,  7, 3), [style.linestyle.dashed])
c.stroke(path.line( 5, 1.5,  5, 4.5), [style.linestyle.dashed])
c.stroke(path.line( 2, 1.5,  2, 4.5), [style.linestyle.dashed])
c.stroke(path.line( 2, 4.5,  5, 4.5), [style.linestyle.dashed])
c.stroke(path.line( 2, 4.5,  4, 6), [style.linestyle.dashed])
c.stroke(path.line( 5, 4.5,  7, 6), [style.linestyle.dashed])


c.stroke(path.circle(5, 4.5,  0.025), [deco.filled([color.grey(0.)])])
c.stroke(path.line( 4, 3,  5, 4.5), [deco.earrow.Large,style.linewidth.THIck])
c.text(5, 4.5, r"\huge$\left(x_1,x_2 ,x_3\right)$" ,[text.halign.boxleft, text.valign.top])

c.stroke(path.line( 4, 3,  1, 0.75), [deco.earrow])
c.stroke(path.line( 4, 3,  8, 3), [deco.earrow])
c.stroke(path.line( 4, 3,  4, 8), [deco.earrow])


c.writePDFfile('fig2-3-center.pdf')

