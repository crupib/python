def my_range(first=0, last=10, step=1):
	number = first
	while number < last:
		yield number
		number += step
def document_it(func):
	def new_function(*args, **kwargs):
		print('Running function:', func.__name__)
		print('Postional arguments:',args)
		print('Keyword arguments:', kwargs)
		result = func(*args, **kwargs)
		print('Result:', result)
		return result
	return new_function
def square_it(func):
	def new_function(*args, **kwargs):
		result = func(*args,**kwargs)
		return result * result
	return new_function
@square_it
@document_it
def add_ints(a,b):
	return a + b

def main():
	ranger = my_range(1,5)
	print (ranger)
	for x in ranger:
		print(x)
#	print(add_ints(3,5))
#	cooler_add_ints = document_it(add_ints)
#	print(cooler_add_ints(3,5))
	print(add_ints(3,5))

    
if __name__ == "__main__":
    main()
