import re
pattern = r".at"
line = "The big fat cat spat on a cat sat on a cat"
result = re.findall(pattern, line)
print(result)
