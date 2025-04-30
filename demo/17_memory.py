import psutil
memory = psutil.virtual_memory()

def ram_usage():
 print(f'Total available memory in gigabytes ' 
 f'{memory.total/(1024**3):.3f}')
 print(f'Total used memory in gigabytes ' 
 f'{memory.used/(1024**3):.3f}')
 print(f'Percentage of memory under use:' 
 f' {memory.percent}%')

ram_usage()
