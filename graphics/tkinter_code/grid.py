from tkinter import *
from tkinter import ttk        
    
root = Tk()
style = ttk.Style(root)
style.theme_use('classic')
style.configure('Test.TLabel',  background = 'yellow')
style.configure('Test1.TLabel', background = 'blue')
style.configure('Test2.TLabel', background = 'green')
style.configure('Test3.TLabel', background = 'orange')

ttk.Label(root, text = 'Yellow', style = 'Test.TLabel').grid(row = 0, column = 2, rowspan = 2, sticky = 'nsew')
ttk.Label(root, text = 'Blue',   style = 'Test1.TLabel').grid(row = 1, column = 0, columnspan = 2, sticky = 'nsew')
ttk.Label(root, text = 'Green',  style = 'Test2.TLabel').grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)
ttk.Label(root, text = 'Orange', style = 'Test3.TLabel').grid(row = 0, column = 1, sticky = 'nsew', ipadx = 25, ipady = 25)

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 3)
root.columnconfigure(2, weight = 1)

root.mainloop()
