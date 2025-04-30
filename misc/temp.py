a = ['mn', 'op']
for i in a:
    i.upper()
print(a)
code = ""
for i in range(4):
   code += str(i)
print(code)
x = 0
a = 4
b = 4
if a > 0:
   if b < 0:
      x = x + 4
   elif a > 4:
      x = x + 3
   else:
      x = x + 2
else:
   x = x + 3
print(x)
num = 23
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
a = 0
if a < 0:
  print(a, "is a negative number")
elif a > 0:
  print(a, "is a positive number")
else:
  print(a, "is not valid here")
x = 1
while True:
   if x % 5 == 0:
      break
   print(x)
   x += 1
print("length ",len(["hi", 11, 22, 33, 44]))
print("reverse")
for i in [8, 6, 4, 2, 0][::-1]:
  print(i)
x = [5, 10]
y = x
y += [15, 20]
print(x)
print(y)
