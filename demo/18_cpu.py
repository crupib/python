import psutil

cpu_core = psutil.cpu_percent(percpu=True)

for cpu, usage in enumerate(cpu_core):
 print(f"# {cpu+1} CPU: {usage}%")
