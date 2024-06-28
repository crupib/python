from mypyx import *

C = mycanvas(x=5, latex=True)

P = [[1, 0], [0, 1],[-1, 0], [0, -1]]
unitcircle = make_polygon(P)
C.stroke(unitcircle,[style.linewidth.thick, deco.filled([color.gray(0.75)])])

C.stroke(path.line(-2, 0, 2, 0),[style.linewidth.thick, deco.earrow])
C.stroke(path.line(0, -2, 0, 2),[style.linewidth.thick, deco.earrow])

C.stroke(path.line(1, -0.1, 1, 0.1))
C.stroke(path.line(-0.1, 1, 0.1, 1))

C.text(-0.1, -0.1, "0" ,[text.halign.right, text.valign.top])
C.text(1.1, -0.1, "1" ,[text.halign.left, text.valign.top])
C.text(-0.1, 1.1, "1" ,[text.halign.right, text.valign.bottom])
C.text(2.1, 0, "$x$" ,[text.halign.left, text.valign.middle])
C.text(0, 2.1, "$y$" ,[text.halign.center, text.valign.bottom])

C.writePDFfile('norm1.pdf')

