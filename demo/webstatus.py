import requests
r = requests.get("https://medium.com/crap")
print(r.status_code) # 200
r = requests.get("https://medium.com/@pythonians")
print(r.status_code) # 200
