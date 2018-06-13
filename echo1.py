def echo(anything):
	'echo returns its input argument'	
	return anything
def print_if_true(thing,check):
	''' 
		Prints the first argument if a second argument is ture;
		The operation is:
			1: Check whether the *second* argument is true.
			2. If it is, print the *first* argument.
	'''
	if check:
		print(thing)
def answer():
	print(42)
def run_something(func):
	func()
print(echo('shit'))
print_if_true('crap',True)
print_if_true('crap',False)
print(echo.__doc__)
print(print_if_true.__doc__)
answer()
run_something(answer)
