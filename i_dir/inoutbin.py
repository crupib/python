inputFile = open('moon.jpg','rb')
outputFile = open('copymoon.jpg','wb')
msg = inputFile.read(10)
while len(msg):
	outputFile.write(msg)
	msg = inputFile.read(10)
inputFile.close()
outputFile.close()
