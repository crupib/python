def add10(x):
  return x + 5

def apply_all(list1, function):
  out = []
  for i in list1:
    out.append(function(i))
  return out

print(apply_all([1,2,3,4,5], add10))
# [11, 12, 13, 14, 15]
