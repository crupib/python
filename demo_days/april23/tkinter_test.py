import tkinter as tk

def convert():
    f = float(f_entry.get())
    c = (f - 32) * 5/9
    c_entry.delete(0, tk.END)
    c_entry.insert(0, str(c))
window = tk.Tk()
window.title("Temperature Converter")
f_label = tk.Label(window, text="Fahrenheit")
f_label.grid(row=0, column=0)
c_label = tk.Label(window, text="Celsius")
c_label.grid(row=1, column=0)
f_entry = tk.Entry(window)
f_entry.grid(row=0, column=1)
c_entry = tk.Entry(window)
c_entry.grid(row=1, column=1)
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=2)
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2)
window.mainloop()
