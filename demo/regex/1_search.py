import re
pattern = r".* .*"
line = "Ada Lovelace"
result = re.search(pattern, line)
print(result)
print(result.group())
print(result.group(0))
