from pyx import *

unit.set(uscale=2, vscale=2, wscale=2, xscale=2)
text.set(text.LatexRunner)
C = canvas.canvas()

x, y = (322, 407)
w = 5
h = w * 407 / 322
x0, y0 = 0, 0.45
x2, y2 = w, h - 0.9
x1, y1 = (x0 + x2)/2, (y0 + y2)/2

bm = bitmap.jpegimage('tablet_disp.jpg')
tablet = bitmap.bitmap(0, 0, bm, width=w, compressmode=None)
C.insert(tablet)

C.stroke(path.line(x0-1.5, y1, x2+1.5, y1),[style.linewidth.Thick, deco.earrow.large])
C.stroke(path.line(x1, y0-1, x1, y2+1.5),[style.linewidth.Thick, deco.earrow.large])
C.text(x1-0.05, y1-0.05, r"$0$" ,[text.halign.right, text.valign.top])


C.stroke(path.line(x2+0.5, y2+0.5, x2, y2),[deco.earrow])
C.text(x2+0.5, y2+0.5, r"$1+i$" ,[text.halign.left, text.valign.bottom])
C.stroke(path.line(x0-0.5, y2+0.5, x0, y2),[deco.earrow])
C.text(x0-0.5, y2+0.5, r"$-1+i$" ,[text.halign.right, text.valign.bottom])
C.stroke(path.line(x0-0.5, y0-0.5, x0, y0),[deco.earrow])
C.text(x0-0.5, y0-0.5, r"$-1-i$" ,[text.halign.right, text.valign.top])
C.stroke(path.line(x2+0.5, y0-0.5, x2, y0),[deco.earrow])
C.text(x2+0.5, y0-0.5, r"$1-i$" ,[text.halign.left, text.valign.top])

C.writePDFfile('tablet_pyx.pdf')

