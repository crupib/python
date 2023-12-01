myDict = {"One":1.35,2.5:"Two Point Five", 3:"+",7.9:2}
print("1.")
print(myDict)
print("2.")
print(myDict["One"])
print("3.")
print(myDict[7.9])
myDict[2.5] = "Two and a Half"
print("4.")
print(myDict)
myDict["New item"] = "I'm new"
print("5.")
print(myDict)
del myDict["One"]
print("6.")
print(myDict)
