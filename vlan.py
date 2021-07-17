import requests
import json

def get_token(dnac="sandboxdnac2.cisco.com"):  
   url = f"https://{dnac}/dna/system/api/v1/auth/token"
   username = "devnetuser"
   password = "Cisco123!"
   headers = {
      "Content-Type": "application/json",
   }
   requests.packages.urllib3.disable_warnings()
   response =  requests.post(url, auth=(username, password), verify=False).json()
   return response["Token"]

def main():
   token = get_token()
   dnac = "sandboxdnac2.cisco.com"
   url = f"https://{dnac}/dna/intent/api/v1/"
   family = "Switches and Hubs"

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }

   device_url = url + "network-device?family=" +  family
   response =  requests.get(device_url, headers=headers, verify=False ).json()
   devices = response["response"]

   device_list = []

   for device in devices:
      print(f"{device['type']} with ID {device['id']}")
      device_list.append(device['id'])
 
   for device_id in device_list:
      print("Investigating device: " + device_id)
      new_interface_url = url + "interface/network-device/" + device_id
      response =  requests.get(new_interface_url, headers=headers, verify=False ).json()
      interfaces = response["response"]
      for interface in interfaces:
         if interface['ipv4Address'] is not None:
            print(f"    {interface['portName']} with IP address {interface['ipv4Address']}")
   response =  requests.get(url, headers=headers, verify=False ).json()

if __name__ == "__main__":
   main()
