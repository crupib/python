import tkinter as tk
from tkinter import ttk
import subprocess
import pandas as pd

def get_ps_ef_output():
    result = subprocess.run(['ps', '-ef'], stdout=subprocess.PIPE)
    lines = result.stdout.decode('utf-8').split('\n')
    headers = lines[0].split()
    data = [line.split(maxsplit=len(headers) - 1) for line in lines[1:] if line]
    df = pd.DataFrame(data, columns=headers)
    return df

def populate_treeview(treeview, dataframe):
    treeview.delete(*treeview.get_children())  # Clear existing data
    treeview['columns'] = list(dataframe.columns)
    treeview['show'] = 'headings'

    for column in treeview['columns']:
        treeview.heading(column, text=column)
        treeview.column(column, width=100)

    for row in dataframe.itertuples(index=False):
        treeview.insert('', 'end', values=row)

def scroll_horizontally(treeview, start_col, step_size):
    cols = list(treeview['columns'])
    num_cols = len(cols)
    
    for item in treeview.get_children():
        values = list(treeview.item(item, 'values'))
        new_values = values[-start_col:] + values[:-start_col]
        treeview.item(item, values=new_values)
    
    start_col = (start_col + step_size) % num_cols
    treeview.after(500, scroll_horizontally, treeview, start_col, step_size)  # Slower scrolling

def update_data(treeview):
    df = get_ps_ef_output()
    populate_treeview(treeview, df)
    treeview.after(10000, update_data, treeview)  # Update data every 10 seconds

root = tk.Tk()
root.title("Scrollable ps -ef Data Window")

tree = ttk.Treeview(root)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
scrollbar.pack(side=tk.BOTTOM, fill="x")

tree.configure(xscrollcommand=scrollbar.set)

df = get_ps_ef_output()
populate_treeview(tree, df)
scroll_horizontally(tree, start_col=0, step_size=1)
update_data(tree)

root.mainloop()

