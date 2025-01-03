import textfsm

show_version = """
Arista DCS-7050TX-64-R
Hardware version:    01.11
Serial number:       JPE16073030
System MAC address:  444c.a876.9746

Software image version: 4.20.15M
Architecture:           i386
Internal build version: 4.20.15M-13793783.42015M
Internal build ID:      f99c7df7-24c7-46f7-8bf9-ddd47ae92f4f

Uptime:                 6 weeks, 0 days, 22 hours and 4 minutes
Total memory:           3818208 kB
Free memory:            2428516 kB
"""

template = open("eos_show_version.fsm")
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(show_version)
print(data)
