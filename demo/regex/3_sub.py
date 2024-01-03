import re
pattern = r"(.*) (.*)"
line = "Ada Lovelace"
result1 = re.sub(pattern, r"\2 \1", line)
result2 = re.sub(pattern, r"Tom", line)
print(result1)
print(result2)
