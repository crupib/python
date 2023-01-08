apple_three = int(input("Apples 3 pointers: "))
apple_two = int(input("Apples 2 pointers: "))
apple_one = int(input("Apples foul pointers: "))
banana_three = int(input("Banana 3 pointers: "))
banana_two = int(input("Banana 3 pointers: "))
banana_one = int(input("Banana 2 pointers: "))
apple_total = apple_three * 3 + apple_two * 2 + apple_one
banana_total = banana_three * 3 + banana_two * 2 + banana_one
if apple_total > banana_total:
  print('A')
elif banana_total > apple_total:
  print('B')
else:
  print('T')
