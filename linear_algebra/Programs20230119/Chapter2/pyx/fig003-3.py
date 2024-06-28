from pyx import *
import os
import sys

p = 0.676 / 0.5

#os.environ['PATH'] =  '/Library/TeX/texbin:${PATH}'

text.set(text.LatexRunner)
text.preamble(r'\usepackage{amsmath}')
text.preamble(r'\usepackage{amsfonts}')
text.preamble(r'\usepackage{amssymb}')
text.preamble(r'\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}')

c = canvas.canvas([trafo.scale(sx=0.5, sy=0.5)])

c.stroke(path.line( 0 * p, 0 * p,  6 * p, 0 * p), [deco.earrow()])
c.stroke(path.line( 0 * p, 0 * p,  0 * p, 6 * p), [deco.earrow()])
c.text(0 * p, 0 * p, r"\huge O" ,[text.halign.right, text.valign.top])

c.text(1 * p, -0.1 * p, r"\huge$1$" ,[text.halign.center, text.valign.top])
c.text(0 * p, 3 * p, r"\huge$x_1$" ,[text.halign.right, text.valign.top])
c.stroke(path.line(1 * p, 0 * p,  1 * p, 3 * p), [style.linewidth.THICK])
c.stroke(path.line(1 * p, 3 * p,  0 * p, 3 * p), [style.linestyle.dashed])

c.text(2 * p, -0.1 * p, r"\huge$2$" ,[text.halign.center, text.valign.top])
c.text(0 * p, 4 * p, r"\huge$x_2$" ,[text.halign.right, text.valign.middle])
c.stroke(path.line(2 * p, 0 * p,  2 * p, 4 * p), [style.linewidth.THICK])
c.stroke(path.line(2 * p, 4 * p,  0 * p, 4 * p), [style.linestyle.dashed])

c.text(5 * p, -0.1 * p, r"\huge$n$" ,[text.halign.center, text.valign.top])
c.text(0 * p, 2 * p, r"\huge$x_n$" ,[text.halign.right, text.valign.middle])
c.stroke(path.line(5 * p, 0 * p,  5 * p, 2 * p), [style.linewidth.THICK])
c.stroke(path.line(5 * p, 2 * p,  0 * p, 2 * p), [style.linestyle.dashed])

c.stroke(path.line(3 * p, 0 * p, 3 * p, 5 * p), [style.linewidth.THICK])
c.stroke(path.line(4 * p, 0 * p, 4 * p, 3.5 * p), [style.linewidth.THICK])



name =  os.path.basename(sys.argv[0]).split('.')[0]

import warnings
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    c.writePDFfile(name + '.pdf', write_textaspath=True)

os.system('rm ./tmp*.*')
