class ParentClass:
	def __init__(self):
		self.a = 1
		print("Parent Class Object Created")
	def someMethod(self):
		print("Hello")
class ChildClass(ParentClass):
	def __init__(self):
		print("Child class object created")
parent = ParentClass()
child  = ChildClass()
print(isinstance(parent,ParentClass))
print(issubclass(ChildClass,ParentClass))
