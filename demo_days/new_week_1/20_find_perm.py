from itertools import permutations

def get_permutations(s: str):
   arr = []
   for i in permutations(s):
      arr.append(''.join(i))
   return arr

print(get_permutations('ABC'))

