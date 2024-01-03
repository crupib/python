import tkinter as tk
from ttkthemes import ThemedTk
root =  ThemedTk(theme="kroc")
root.geometry('300x400')
mybutton = tk.Button(root,text='Hello world!')
mybutton.place(relx=0.5,rely=0.5, anchor="center")
root.mainloop()
