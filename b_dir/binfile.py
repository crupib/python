import os
inputFile =  open('jpeg_43.jpg','rb')
outputFile = open('myjpeg.jpg', 'wb')
msg = inputFile.read(10)
while len(msg):
	outputFile.write(msg)
	msg = inputFile.read(10)
inputFile.close()
outputFile.close()
os.rename('myjpeg.jpg', 'micro.jpg')
os.remove('micro.jpg')
