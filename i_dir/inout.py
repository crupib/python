inputFile = open('data.txt', 'r')
outputFile = open('dataout.txt', 'w')
msg = inputFile.read(10)
while len(msg):
    outmsg = msg.replace('\r', '').replace('\n', '')
    outputFile.write(outmsg)
    msg = inputFile.read(10)
inputFile.close()
outputFile.close()
