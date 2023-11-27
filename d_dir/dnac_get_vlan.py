import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
urllib3.disable_warnings()
#Public username and password from Cisco website.
USERNAME="devnetuser"
PASSWORD="Cisco123!"
# API URL TO GET A LIST OF NETWORK DEVICES
url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"
def get_auth_token():
    url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
    resp = requests.post(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
    token = resp.json()['Token']
    return token
payload = {}
# WE MUST ADD OUR AUTHENTICATION TOKEN TO THE HEADERS
# First get token
temp_token = get_auth_token()
headers = {
    'X-Auth-Token': temp_token 
 }
response = requests.request("GET", url, verify=False, headers=headers, data=payload)

# TAKE THE RESPONSE AND TURN IT INTO PYTHON OBJECTS
raw_output = json.loads(response.text)

# raw_output IS A DICTIONARY. TAKE THE VALUE OF response AND ASSIGN TO devices
devices = raw_output["response"]
id = [] 
# ITERATE THROUGH THE LIST TO PRINT OUT HOSTNAMES OF DEVICES
for device in devices:
#    print("ID: {}".format(device["id"]),"Hostname: {}".format(device["hostname"]),"MACADDRESS: {}".format(device["macAddress"]))
    id.append(device["id"])
for deviceid in id:
   payload = {}
   url=f"https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device/{deviceid}/vlan"
   response = requests.request("GET", url, verify=False, headers=headers, data=payload)
   raw_output = json.loads(response.text)  
   print(raw_output)
   vlans = raw_output["response"]
   #print(vlans)
   for vlan in raw_output:
         if response == 'no
         print("vlan #: {}".format(vlan["vlanNumber"]))
