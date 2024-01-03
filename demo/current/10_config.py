import configparser

configParser= configparser.ConfigParser() # Creating a configParser object
filename= "tempConfig.ini"
configParser.read(filename)    # Reading the config file
Servers= configParser.sections()    # Getting sections from config file
print (Servers)                     # Printing the Sections (Servers)
Servers= configParser.sections()    # Getting sections from config file
host= configParser[Servers[0]]['host']  # Getting item using the key host
port= configParser[Servers[0]]['port']  # Getting item using the key port
print(f"Host: {host} port: {port}")
