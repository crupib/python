from pyx import *

text.set(text.LatexRunner)
C = canvas.canvas()

C.stroke(path.line(-5, 0, 5, 0),[style.linewidth.Thick, deco.earrow.large])
C.stroke(path.line(0, -0.1, 0, 0.1))
C.stroke(path.line(1, -0.1, 1, 0.1))
C.text(0, -0.2, r"\huge 0" ,[text.halign.center, text.valign.top])
C.text(1, -0.2, r"\huge 1" ,[text.halign.center, text.valign.top])
C.stroke(path.circle(2, 0, 0.05), [deco.filled([color.grey.black])])
C.text(2, -0.3, r"\huge $x$" ,[text.halign.center, text.valign.top])
C.writePDFfile('real.pdf')

