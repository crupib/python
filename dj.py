import requests
url = 'http://192.168.99.210/api/extras/scripts/Full_inventory.Myscript/'
headers = {'Authorization':'Token="1aa4f3d30e24b5abd24d388394dab69beda99e87"'}
r = requests.post(url, headers=headers)
print(r.status_code)
