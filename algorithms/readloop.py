f = open('data.txt','a')
f.write('\nThis sentence will be appended.')
f.write('\nPython is Fun!\n')
f.close()
f = open('data.txt','r')
for line in f:
	print(line,end='',flush=True)
f.close()
