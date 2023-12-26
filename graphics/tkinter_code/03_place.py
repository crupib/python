#!/usr/bin/python3
# place.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()
root.geometry('640x480+200+200')
style = ttk.Style(root)
style.theme_use('classic')
style.configure('Test.TLabel', background= 'yellow')
style.configure('Test1.TLabel', background= 'blue')
style.configure('Test2.TLabel', background= 'green')
style.configure('Test3.TLabel', background= 'orange')

ttk.Label(root, text = 'Yellow', style = 'Test.TLabel').place(x = 100, y = 50, width = 100, height = 50)
ttk.Label(root, text = 'Blue',   style = 'Test1.TLabel').place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.5, relheight = 0.5)
ttk.Label(root, text = 'Green',  style = 'Test2.TLabel').place(relx = 0.5, x = 100, rely = 0.5, y = 50)
ttk.Label(root, text = 'Orange', style = 'Test3.TLabel').place(relx = 1.0, x = -5, y = 5, anchor = 'ne')

root.mainloop()
