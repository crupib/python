import re
pattern = r".at"
line = "The big fat cat sat on a cat"
result = re.findall(pattern, line)
print(result)
