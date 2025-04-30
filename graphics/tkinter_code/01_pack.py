from tkinter import *
from tkinter import ttk
root = Tk()
style = ttk.Style(root)
style.theme_use('classic')
style.configure('Test.TLabel', background= 'yellow')
style.configure('Test1.TLabel', background= 'blue')
style.configure('Test2.TLabel', background= 'red')
ttk.Label(root, text = "Hello, Tkinter!", style= 'Test.TLabel').pack(side = LEFT, anchor = 'nw')
ttk.Label(root, text = "Hello, Tkinter!", style= 'Test1.TLabel').pack(side = LEFT, padx = 10, pady = 10)
ttk.Label(root, text = "Hello, Tkinter!", style= 'Test2.TLabel').pack(side = LEFT, ipadx = 10, ipady = 10)

for widget in root.pack_slaves():
    widget.pack_configure(fill = BOTH, expand = True)
    print(widget.pack_info())
root.mainloop()
