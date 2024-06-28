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

c.stroke(path.line( 0 * p, 1 * p,  6 * p, 1 * p), [deco.earrow()])
c.stroke(path.line( 1 * p, 0 * p,  1 * p, 6 * p), [deco.earrow()])

c.stroke(path.circle(4 * p, 3 * p,  0.025 * p), [deco.filled([color.grey(0.)])])

c.stroke(path.line( 1 * p, 1 * p,  4 * p, 3 * p), [deco.earrow.Large ,style.linewidth.THIck])

c.stroke(path.line( 4 * p, 1 * p,  4 * p, 3 * p), [style.linestyle.dashed])
c.stroke(path.line( 1 * p, 3 * p,  4 * p, 3 * p), [style.linestyle.dashed])

c.text(0.9 * p, 0.9 * p, r"\huge O" ,[text.halign.boxright, text.valign.top])
#c.text(4 * p, 1 * p, r"\huge$x_1$" ,[text.halign.boxcenter, text.valign.top])
c.text(4 * p, 0.9 * p, r"\huge$x_1$" ,[text.halign.boxcenter, text.valign.top])
#c.text(1 * p, 3 * p, r"\huge$x_2$" ,[text.halign.boxright, text.valign.middle])
c.text(0.9 * p, 3 * p, r"\huge$x_2$" ,[text.halign.boxright, text.valign.middle])

c.text(4 * p, 3 * p, r"\huge$\left(x_1,x_2\right)$" ,[text.halign.boxleft, text.valign.bottom])



name =  os.path.basename(sys.argv[0]).split('.')[0]

import warnings
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    c.writePDFfile(name + '.pdf', write_textaspath=True)

os.system('rm ./tmp*.*')
