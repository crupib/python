#!/usr/local/bin/python3
import sys,re
[sys.stdout.write(re.sub('google', 'gaggle', line)) for line in sys.stdin]
