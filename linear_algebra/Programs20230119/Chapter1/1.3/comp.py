from pyx import *

text.set(text.LatexRunner)
C = canvas.canvas()

C.stroke(path.circle(0, 0, 1),[style.linewidth.thick,
                               deco.filled([color.gray(0.75)])])
C.stroke(path.line(-5, 0, 5, 0),[style.linewidth.Thick, deco.earrow.large])
C.stroke(path.line(0, -5, 0, 5),[style.linewidth.Thick, deco.earrow.large])
C.text(-0.1, -0.1, r"\huge 0" ,[text.halign.right, text.valign.top])
C.text(1, -0.2, r"\huge 1" ,[text.halign.left, text.valign.top])
C.text(-0.2, 1, r"\huge $i$" ,[text.halign.right, text.valign.bottom])
C.stroke(path.circle(2, 3, 0.05), [deco.filled([color.grey.black])])
C.text(2.1, 3.1, r"\huge $z=x+iy$" ,[text.halign.left, text.valign.bottom])
C.stroke(path.line(2, 3, 2, 0),[style.linewidth.thick,
                                style.linestyle.dashed])
C.stroke(path.line(2, 3, 0, 3),[style.linewidth.thick,
                                style.linestyle.dashed])
C.stroke(path.line(2, -0.1, 2, 0))
C.text(2, -0.3, r"\huge $x$" ,[text.halign.center, text.valign.top])
C.stroke(path.line(-0.1, 3, 0, 3))
C.text(-0.1, 3, r"\huge $iy$" ,[text.halign.right, text.valign.middle])
C.writePDFfile('comp.pdf')

