import configparser

class HostConfig:
    def __init__(self, configFile):
        self.configFile= configFile
        self.config= configparser.ConfigParser()
        
    def readConfig(self):
        # Reading the config file
        self.config.read(self.configFile)
    
    def getServers(self):
        # Returning all the sections defined in the config file
        return self.config.sections()
    
    def getData(self, host, key):
        # Getting the values from the particular section (host) 
        # by using the key       
        return self.config[host][key]
    
    def getHostDetails(self, host):
        # Getting all the values defined under the given section (host).
        # Assuming the keys are known and fixed.
        hostdata= self.config[host]
        return hostdata['host'],hostdata['port'],hostdata['username'],hostdata['password']

def main():
   hostConfig= HostConfig('tempConfig.ini')  # creating object of HostConfig
   hostConfig.readConfig()                   # Reading config file 

   Servers= hostConfig.getServers()       # Getting the list of sections (servers)
   print("Servers: ",Servers)

   print("Server 0 data: \n",hostConfig.getHostDetails(Servers[0]))  # Getting items for Section No 0

   print("Server1: Host ",hostConfig.getData(Servers[1], 'host'))  # Getting item for Section No 1
   print("Server1: Port ",hostConfig.getData(Servers[1], 'port'))  # Getting item for Section No 1

if __name__ == "__main__":
    main()
