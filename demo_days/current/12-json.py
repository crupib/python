import json # import json

data = ["Amit", "Raghav", "Utkarsh", "Akash"] 
json_data = json.dumps(data) # dumping data to json from list with json.dumps()
print(data)

data = [["Amit", "Raghav", "Utkarsh", "Akash"], ["Delhi", "Mumbai", "Hyderabad", "Chennai"]]
json_data = json.dumps(data)

print(json_data)
data = [{"Amit": "Delhi"}, {"Utkarsh": "Hyderabad"}, {"Raghav": "Mumbai"}]
json_data = json.dumps(data)

print(json_data)
