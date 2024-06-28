from pyx import *
import os
import sys

p = 0.666 / 0.5

#os.environ['PATH'] =  '/Library/TeX/texbin:${PATH}'

text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

c = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])

c.text(3.9 * p, 2.9 * p, r"\huge O" ,[text.halign.boxleft, text.valign.top])


c.stroke(path.line( 2 * p, 1.5 * p,  5 * p, 1.5 * p), [style.linestyle.dashed])
c.text(2 * p, 1.5 * p, r"\huge$x_1$" ,[text.halign.boxright, text.valign.bottom])

c.stroke(path.line( 5 * p, 1.5 * p,  7 * p, 3 * p), [style.linestyle.dashed])
#c.text(7 * p, 3 * p, r"\huge$x_2$" ,[text.halign.boxleft, text.valign.top])
c.text(7 * p, 2.9 * p, r"\huge$x_2$" ,[text.halign.boxleft, text.valign.top])

c.stroke(path.line( 4 * p, 6 * p,  7 * p, 6 * p), [style.linestyle.dashed])
#c.text(4 * p, 6 * p, r"\huge$x_3$" ,[text.halign.boxright, text.valign.middle])
c.text(4 * p, 6.2 * p, r"\huge$x_3$" ,[text.halign.boxright, text.valign.middle])

c.stroke(path.line( 7 * p, 6 * p,  7 * p, 3 * p), [style.linestyle.dashed])
c.stroke(path.line( 5 * p, 1.5 * p,  5 * p, 4.5 * p), [style.linestyle.dashed])
c.stroke(path.line( 2 * p, 1.5 * p,  2 * p, 4.5 * p), [style.linestyle.dashed])
c.stroke(path.line( 2 * p, 4.5 * p,  5 * p, 4.5 * p), [style.linestyle.dashed])
c.stroke(path.line( 2 * p, 4.5 * p,  4 * p, 6 * p), [style.linestyle.dashed])
c.stroke(path.line( 5 * p, 4.5 * p,  7 * p, 6 * p), [style.linestyle.dashed])


c.stroke(path.circle(5 * p, 4.5 * p,  0.025 * p), [deco.filled([color.grey(0.)])])
c.stroke(path.line( 4 * p, 3 * p,  5 * p, 4.5 * p), [deco.earrow.Large,style.linewidth.THIck])
c.text(5 * p, 4.5 * p, r"\huge$\left(x_1,x_2 ,x_3\right)$" ,[text.halign.boxleft, text.valign.top])

c.stroke(path.line( 4 * p, 3 * p,  1 * p, 0.75 * p), [deco.earrow])
c.stroke(path.line( 4 * p, 3 * p,  8 * p, 3 * p), [deco.earrow])
c.stroke(path.line( 4 * p, 3 * p,  4 * p, 8 * p), [deco.earrow])


name =  os.path.basename(sys.argv[0]).split('.')[0]

import warnings
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    c.writePDFfile(name + '.pdf', write_textaspath=True)

os.system('rm ./tmp*.*')
