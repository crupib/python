import requests
from requests.auth import HTTPBasicAuth
#from dnac_config import DNAC_IP, USERNAME, PASSWORD
USERNAME="devnetuser"
PASSWORD="Cisco123!"

requests.packages.urllib3.disable_warnings()

def get_auth_token():
    url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
    resp = requests.post(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
    token = resp.json()['Token']
#    print("Token Retrieved: {}".format(token))
    return token

if __name__ == "__main__":
 mytoken=get_auth_token()
 print(mytoken)
