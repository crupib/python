inputFile =  open('data.txt','r')
outputFile = open('myoutputfile.txt', 'w')
msg = inputFile.read(10)
while len(msg):
	outputFile.write(msg)
	msg = inputFile.read(10)
inputFile.close()
outputFile.close()
