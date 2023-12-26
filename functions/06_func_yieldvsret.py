def test2():
  yield 1
  yield 2
  yield 3

for i in test2():
  print(i)
