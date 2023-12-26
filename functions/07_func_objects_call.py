class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __call__(self):
    return  'apple'

remy = Dog('remy', 3)
print(remy())
