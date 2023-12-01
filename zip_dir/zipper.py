import zipfile

Zippy = zipfile.ZipFile('pretty.zip', 'w')
Zippy.write("./pretty.py")
Zippy.close()                                                                          
