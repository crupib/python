fruits = ['apple', 'orange', 'pear']

def condition_function(element):
  return len(element)

fruits.sort(key=condition_function)

print(fruits)
