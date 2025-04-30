import tkinter as tk
from tkinter import ttk
import subprocess
import pandas as pd
import threading
import queue

def get_ps_ef_output():
    result = subprocess.run(['ps', '-ef'], stdout=subprocess.PIPE)
    lines = result.stdout.decode('utf-8').split('\n')
    headers = lines[0].split()
    data = [line.split(maxsplit=len(headers) - 1) for line in lines[1:] if line]
    df = pd.DataFrame(data, columns=headers)
    return df

def tail_f_log(file_path, output_queue):
    process = subprocess.Popen(['tail', '-f', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in iter(process.stdout.readline, b''):
        output_queue.put(line.decode('utf-8').strip())

def get_log_data_from_queue(output_queue):
    data = []
    while not output_queue.empty():
        line = output_queue.get()
        data.append(line.split(maxsplit=5))
    headers = ["Date", "Time", "User", "Database", "PID", "Message"]
    df = pd.DataFrame(data, columns=headers)
    return df

def populate_treeview(treeview, dataframe):
    treeview.delete(*treeview.get_children())  # Clear existing data
    treeview['columns'] = list(dataframe.columns)
    treeview['show'] = 'headings'

    for column in treeview['columns']:
        treeview.heading(column, text=column)
        treeview.column(column, width=150)

    for row in dataframe.itertuples(index=False):
        treeview.insert('', 'end', values=row)

def scroll_horizontally(treeview, start_col, step_size):
    cols = list(treeview['columns'])
    num_cols = len(cols)
    
    if num_cols > 0:
        for item in treeview.get_children():
            values = list(treeview.item(item, 'values'))
            new_values = values[-start_col:] + values[:-start_col]
            treeview.item(item, values=new_values)
        
        start_col = (start_col + step_size) % num_cols
    treeview.after(1000, scroll_horizontally, treeview, start_col, step_size)  # Slower scrolling

def update_data_ps(treeview):
    df = get_ps_ef_output()
    populate_treeview(treeview, df)
    treeview.after(15000, update_data_ps, treeview)  # Update data every 15 seconds

def update_data_postgres(treeview, output_queue):
    df = get_log_data_from_queue(output_queue)
    if not df.empty:
        populate_treeview(treeview, df)
    treeview.after(1000, update_data_postgres, treeview, output_queue)  # Check for new log data every second

root = tk.Tk()
root.title("Scrollable Data Windows")

# First Treeview (ps -ef output)
tree1 = ttk.Treeview(root)
tree1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar1 = ttk.Scrollbar(root, orient="horizontal", command=tree1.xview)
scrollbar1.pack(side=tk.BOTTOM, fill="x")

tree1.configure(xscrollcommand=scrollbar1.set)

# Second Treeview (PostgreSQL log)
tree2_frame = tk.Frame(root, bg="lightblue")
tree2_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tree2 = ttk.Treeview(tree2_frame)
tree2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar2 = ttk.Scrollbar(tree2_frame, orient="horizontal", command=tree2.xview)
scrollbar2.pack(side=tk.BOTTOM, fill="x")

tree2.configure(xscrollcommand=scrollbar2.set)

# Queue for PostgreSQL log output
output_queue = queue.Queue()

# Start tail -f in a separate thread
log_thread = threading.Thread(target=tail_f_log, args=("/usr/local/var/log/postgresql@14.log", output_queue))
log_thread.daemon = True
log_thread.start()

df_ps = get_ps_ef_output()
populate_treeview(tree1, df_ps)

scroll_horizontally(tree1, start_col=0, step_size=1)
scroll_horizontally(tree2, start_col=0, step_size=1)

update_data_ps

