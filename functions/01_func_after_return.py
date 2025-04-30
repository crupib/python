def test():
  try:
    print('apple')
    print('orange')
    return 1
  finally:
    print('pear')

test()
