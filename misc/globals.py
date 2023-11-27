def amazing():
	'''THis is the amazing function.
	Want to see it again?'''
	print('This function is named:',amazing.__name__)
	print('And its docstring is:',amazing.__doc__)

def print_global():
	print('inside print_global:',animal)
def change_local():
	animal = 'wombat'
#	print('inside change_local:',animal,id(animal))
	print('locals:',locals())
def change_and_print_global():
	global animal
	animal = 'wombat'
#	print('inside change_and_print_global:', animal)
def main():
	animal = 'fruitbat'
#	print('at the top level:',animal)
#	print_global()
	change_local()
#	print(id(animal))
#	print(animal)
#	change_and_print_global()
#	print('global after change from local')
#	print(id(animal))
#	print(animal)
	print('globals:',globals())
	amazing()

    
if __name__ == "__main__":
    main()
