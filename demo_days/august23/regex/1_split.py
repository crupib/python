import re
pattern = r"cat"
line = "The big fat cat sat on a cat"
result = re.split(pattern, line)
print(result)
