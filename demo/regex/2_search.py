import re
pattern = r"(.*) (.*)"
line = "Ada Lovelace"
result = re.search(pattern, line)
print(result)
print(result.groups())
print(result.group(0))
print(result.group(1))
print(result.group(2))

