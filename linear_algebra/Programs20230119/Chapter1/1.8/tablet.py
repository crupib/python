from tkinter import Tk, Button, Canvas

def point(x, y):
    return C.create_oval(x - 1, y - 1, x + 1, y + 1, fill='black')

def PushButton(event):
    x, y = event.x, event.y
    Segs.append([((x, y), point(x, y))])

def DragMouse(event):
    x, y = event.x, event.y
    Segs[-1].append(((x, y), point(x, y)))

def Erase():
    if Segs != []:
        seg = Segs.pop()
        for p in seg:
            C.delete(p[1])

def Save():
    if Segs != []:
        L = []
        for seg in Segs:
            for (x, y), _ in seg:
                L.append((x - 160) / 160 + 1j * (160 - y) / 160)
        with open(filename, 'w') as fd:
            fd.write(repr(L))
        print('saved!')

filename = 'tablet.txt'
Segs = []
tk = Tk()
Button(tk, text="erase", command=Erase).pack()
C = Canvas(tk, width=320, height=320, bg='white')
C.pack()
C.bind("<Button-1>", PushButton)
C.bind("<B1-Motion>", DragMouse)
Button(tk, text="save", command=Save).pack()
tk.mainloop()
