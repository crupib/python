import re
pattern = r"Ada"
line = "Ada Lovelace"
result = re.sub(pattern, r"Tom", line)
print(result)
