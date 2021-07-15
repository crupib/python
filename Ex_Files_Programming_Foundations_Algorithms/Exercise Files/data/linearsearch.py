def LinearSearch(list, item, position):
  index = 0
  found = []
  while index < len(list):
    if list[index][position] == item:
      found.append(list[index])
      index = index + 1
    else:
      index = index + 1
  return found
