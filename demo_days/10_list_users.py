#!/usr/local/bin/python3
print ('\n'.join(line.split(":",1)[0] for line in open("/etc/passwd")))
